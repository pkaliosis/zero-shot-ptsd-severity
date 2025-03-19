import logging
import os
import time
import pandas as pd
from tqdm import tqdm

from src import parse_api_run_args, get_api_key, OpenAICommunicator
#from prompt_templates import templates
from prompt_ptsd_templates import templates

import pickle
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import getpass
from transformers import AutoTokenizer

### **Encryption Initialization Function**
def initialize_encryption():
    """
    Initializes encryption by:
    1. Prompting for a password securely
    2. Generating a random salt
    3. Deriving an encryption key from the password using PBKDF2
    """
    password = getpass.getpass("Enter a password for encryption: ").encode()
    salt = os.urandom(16)  # Generate a random salt

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend(),
    )
    key = kdf.derive(password)  # Derive encryption key from password
    return key, salt


if __name__ == "__main__":
    args = parse_api_run_args()
    
    """if args.expt_name not in templates:
        raise ValueError("Experiment name {} not found in templates.\n Choices: {}".format(args.expt_name, list(templates.keys())))"""
            
    run_folder_path = args.save_folder_path
    # prompts_dir = os.path.join(run_folder_path, "expts/prompts")
    responses_dir = os.path.join(run_folder_path, "expts/responses")
    logs_dir = os.path.join(run_folder_path, "expts/logs")
    
    # makedir if not exists
    os.makedirs(run_folder_path, mode=700, exist_ok=True)
    # os.makedirs(prompts_dir, mode=770, exist_ok=True)
    os.makedirs(responses_dir, mode=700, exist_ok=True)
    os.makedirs(logs_dir, mode=700, exist_ok=True)
    
    prefix = 'demo_' if args.demo else 'expt_'
    expt_metainfo = '.'.join([prefix+args.openai_model_name, args.expt_name])
    log_file_path = os.path.join(run_folder_path, "expts/logs/{}.log".format(expt_metainfo))
    logging.basicConfig(level=logging.INFO, filename=log_file_path, 
                    format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
    print ("Logging to {}".format(log_file_path))
    logging.info("Starting Experiment {}".format(args.expt_name))
    
    args_dict = args.__dict__
    logging.info("Args: {}".format(args))
    
    if not args.deepseek:
        args.api_key = get_api_key(api_key_file=".api_key", api_key_name=args.api_key_name)
        logging.info("API Key loaded")
    
    # prompts_file_path = os.path.join(prompts_dir, "{}.csv".format(expt_metainfo))
    # logging.info("Storing prompts to {}".format(prompts_file_path))
    responses_file_path = os.path.join(responses_dir, "{}.csv".format(expt_metainfo))
    logging.info("Storing responses to {}".format(responses_file_path))

    # Initialize encryption
    encryption_key, encryption_salt = initialize_encryption()

    args_dict["encryption_key"] = encryption_key
    args_dict["encryption_salt"] = encryption_salt
    args_dict["out_pickle_path"] = "./out/{}.csv".format(expt_metainfo)
    args_dict["model_path"] = args.model_path

    #tokenizer_path = "/home/pkaliosis1/pretrained/DeepSeek-R1-Distill-Llama-70B-hf"
    tokenizer_path = "/home/pkaliosis1/pretrained/Llama-3.3-70B-Instruct/snapshots/snapshots"
    print("Tokenizer path:", args.model_path)
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
        
    openai_communicator = OpenAICommunicator(args_dict, tokenizer)
    logging.info("OpenAI Communicator initialized")
    
    # Load instruction
    #instruction = templates["ptsd_wo-reasoning_w-subscales_wo-questions"]

    # Load the encrypted file
    with open("tokenized_data_encrypted.pkl", "rb") as f:
        file_content = f.read()

    # Extract salt, nonce, tag, and encrypted data
    salt = file_content[:16]
    nonce = file_content[16:28]
    tag = file_content[28:44]
    encrypted_data = file_content[44:]

    # Get password securely
    password = getpass.getpass("Enter the password for decryption: ").encode()

    # Generate the same key from the password using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend(),
    )
    key = kdf.derive(password)

    # Decrypt data using AES-GCM
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Deserialize pickle data
    tokenized_dict = pickle.loads(decrypted_data)

    print("Decryption successful! Loaded tokenized data.")

    video_ids, decrypted_token_ids = list(tokenized_dict.keys()), list(tokenized_dict.values())
    logging.info("Loaded {} rows of data for Inference.".format(len(video_ids)))
    
    query_response_time = []
    start_time = time.time()
    output_list = []
    for idx in tqdm(range(len(video_ids)), desc="Running inference with {}".format(args.openai_model_name)):
        video_id, input_transcript = video_ids[idx], decrypted_token_ids[idx][0]
        if (len(input_transcript) == 0):
            continue
        
        input_text = tokenizer.decode(input_transcript, skip_special_tokens=True)
        if (len(input_text.split(" ")) < 150) or (len(input_text.split(" ")) > 3000):
            print("Skipping due to not enough words...")
            continue
        
        phase = str(video_id.split("_")[-1])
        instruction = templates[f"ptsd_wo-reasoning_wo-subscales_wo-questions"]
        instruction_with_text = instruction.format(text=input_text)
        input_prompt = [
            # {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": instruction_with_text}
        ]
        query_start_time = time.time()
        response_text = openai_communicator.run_inference(input_prompt, video_id)
        query_response_time.append(time.time() - query_start_time)
    end_time = time.time()
    
    total_time = round(end_time - start_time, 2)
    avg_response_time = round(sum(query_response_time)/len(query_response_time), 2)
    logging.info("Total time taken for inference: {}".format(total_time))
    logging.info("Average time taken for inference of: {}".format(avg_response_time))
    
    """output_df = pd.DataFrame(output_list)
    output_df.to_csv(responses_file_path, index=False)
    logging.info("Responses saved to {}".format(responses_file_path))"""
    
    logging.info("Experiment {} completed".format(args.expt_name))
    print ("Experiment {} completed".format(args.expt_name))