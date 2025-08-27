# -*- coding: utf-8 -*-
__author__ = """Yash Kumar Lal, Github@ykl7
                Adithya V Ganesan, Github@adithya8"""

import os
import openai
from openai import OpenAI
import pickle
import time
import os
import hashlib
import atexit
import requests
import getpass
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import re
from vllm import LLM
from vllm import SamplingParams
from openai import AzureOpenAI
from dotenv import load_dotenv

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError



#os.environ["CUDA_VISIBLE_DEVICES"] = ""
"""
python3 main.py --expt_name ptsd_w-reasoning_w-subscales_wo-questions --save_folder_path ./out/ --deepseek --openai_model_name DeepSeek-R1-Distill-Llama-70B-hf --model_path /home/pkaliosis1/pretrained/DeepSeek-R1-Distill-Llama-70B-hf --max_tokens 3500 --output_pickle_path /home/pkaliosis1/deepseek-ptsd/gpt4-depression-schema/out/expts/responses/llama70_w_reasoning_w_defs_wo_questions_temp06_r3.pkl --cache_path /home/pkaliosis1/deepseek-ptsd/gpt4-depression-schema/out/cache/llama70_cache_w_reas_w_defs_wo_questions_temp06_r3.pkl --output_pickle_scores_path /home/pkaliosis1/deepseek-ptsd/gpt4-depression-schema/out/expts/responses/llama70_w_reasoning_w_defs_wo_questions_scores_temp06_r3.pkl --port 8000 --temperature 0.6
"""
openai_api_key = "EMPTY"
openai_api_base = f"http://localhost:8001/v1"


client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

load_dotenv()


class OpenAICommunicator:

    def __init__(self, options, tokenizer):

        atexit.register(self.cleanup)

        #openai.api_key = options["api_key"]
        self.model_name = options["openai_model_name"]
        self.max_tokens = options["max_tokens"]
        self.cache_path = options["cache_path"]
        self.temp = options["temperature"]
        self.top_p = options["top_p"]
        self.frequency_penalty = options["frequency_penalty"]
        self.presence_penalty = options["presence_penalty"]
        self.encryption_key = options["encryption_key"]
        self.encryption_salt = options["encryption_salt"]
        self.PICKLE_NAME = options["output_pickle_path"]
        self.PICKLE_NAME_SCORES = options["output_pickle_scores_path"]
        self.port = options["port"]
        self.model_path = options["model_path"]
        self.tokenizer = tokenizer
        self.cached_responses = self.load_cache_if_exists()
        self.client = AzureOpenAI(
            api_version="2024-12-01-preview",
            azure_endpoint="https://azopenai-psyc-wtcwellness.openai.azure.com/",
            api_key=os.getenv("AZURE_API_KEY"),
        )
        

        

    def load_cache_if_exists(self):
        if os.path.exists(self.cache_path):
            with open(self.cache_path, 'rb') as handle:
                cache_file = pickle.load(handle)
                return cache_file
        else:
            os.makedirs(os.path.dirname(self.cache_path), exist_ok=True)
            return {}

    def cleanup(self):
        # works similar to a destructor but does not offload builtins.open method.
        print(f"\nFinal cleanup cache saving...", end="...")
        with open(self.cache_path, 'wb') as handle:
            pickle.dump(self.cached_responses, handle)

    def make_openai_api_call(self, prompt, video_id, llm=None):
        batched = False
        try:
            if self.model_name in ['gpt-3.5-turbo', 'gpt-4', 'gpt-4-1106-preview', 'gpt-4-0613', 'o3-mini', 'gpt-4o-mini', 'gpt-5']:

                
                #deployment = "o3-mini"
                deployment = "gpt-5"

                print("Calling GPT-5...")

                response = self.client.chat.completions.create(
                    messages=prompt,
                    max_completion_tokens=10000,
                    model=deployment,
                    #reasoning_effort="high"
                )

                #print("Usage o3-mini:", response.usage)

                #return self.parse_chatgpt_api_response(response)
                return response.choices[0].message.content, response.choices[0].message
                
            elif self.model_name in ["gpt-oss"]:
                client = OpenAI(
                    base_url="http://localhost:8000/v1",
                    api_key="EMPTY"
                )

                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=prompt,
                    max_completion_tokens=10000,
                )

                print("gpt-oss response:", response.choices[0].message.content)

                return response.choices[0].message.content, response.choices[0].message

            elif self.model_name in ["Meta-Llama-3.1-405B-Instruct"]:
                endpoint = "https://pkali-m91n263l-eastus2.services.ai.azure.com/models"
                model_name = "Meta-Llama-3.1-405B-Instruct"

                client = ChatCompletionsClient(
                    endpoint=endpoint,
                    credential=AzureKeyCredential(os.getenv("AZURE_AI_API_KEY")),
                    api_version="2024-05-01-preview"
                )
                """response = client.complete(
                    messages=[
                        UserMessage(content=prompt)
                    ],
                    max_tokens=10000,
                    temperature=0.0,
                    model=model_name
                )"""
                max_retries = 3
                for attempt in range(max_retries):
                    try:
                        # Your call to the ChatCompletionsClient
                        response = client.complete(
                            messages=[
                                UserMessage(content=prompt)
                            ],
                            max_tokens=20000,
                            temperature=0.0,
                            model=model_name
                        )
                        break  # Break if successful
                    except HttpResponseError as e:
                        print(f"Attempt {attempt+1} failed with error: {e}")
                        time.sleep(2 ** attempt)  # Exponential backoff
                else:
                    print("Failed after several retries.")
                print("Llama405b Usage:", response.usage)
                return response.choices[0].message.content, response.choices[0].message
            
            elif self.model_name in ["DeepSeek-R1"]:
                endpoint = "https://pkali-m91n263l-eastus2.services.ai.azure.com/models"
                model_name = "DeepSeek-R1"

                client = ChatCompletionsClient(
                    endpoint=endpoint,
                    credential=AzureKeyCredential(os.getenv("AZURE_AI_API_KEY")),
                )
                response = client.complete(
                    messages=[
                        UserMessage(content=prompt)
                    ],
                    max_tokens=10000,
                    temperature=0.0,
                    model=model_name
                )
                print("DeepSeek-r1 Usage:", response.usage)
                return response.choices[0].message.content, response.choices[0].message


            elif "DeepSeek" in self.model_name:
                # Prepare API request payload
                payload = {
                    "prompt": prompt,
                    "temperature": self.temp,  # Adjust as needed
                    "max_tokens":self.max_tokens,
                    "top_p":self.top_p,
                    "frequency_penalty":self.frequency_penalty,
                    "presence_penalty":self.presence_penalty
                }
                print(self.model_path)
                """response = client.chat.completions.create(model=self.model_path,
                                                            messages=prompt,
                                                            temperature=self.temp,
                                                            max_tokens=self.max_tokens,
                                                            top_p=self.top_p,
                                                            frequency_penalty=self.frequency_penalty,
                                                            presence_penalty=self.presence_penalty
                                                        )"""
                client = OpenAI(
                        api_key=openai_api_key,
                        base_url=openai_api_base,
                    )
                max_retries = 3
                for attempt in range(max_retries):
                    try:
                        # Your call to the ChatCompletionsClient
                        response = client.chat.completions.create(model=self.model_path,
                                                            messages=prompt,
                                                            temperature=self.temp,
                                                            max_tokens=self.max_tokens,
                                                            top_p=self.top_p,
                                                            frequency_penalty=self.frequency_penalty,
                                                            presence_penalty=self.presence_penalty
                                                        )
                        break  # Break if successful
                    except Exception as e:
                        print(f"Attempt {attempt+1} failed with error: {e}")
                        time.sleep(2 ** attempt)  # Exponential backoff
                else:
                    print("Failed after several retries.")

                # Send request to vLLM API
                #response = requests.post("http://localhost:8000/v1/chat/completions", headers=headers, json=data)
                
                
                resp = response.choices[0].message.content
                print("resp:", resp)
                if len(resp) > 0:
                    return resp, response
                else:
                    print(f"Error for {video_id}: {response}")
            elif ("Llama" in self.model_name):
                print("the model name is:", self.model_name)
                if "Instruct" in self.model_name:
                    # Prepare API request payload
                    payload = {
                        "prompt": prompt,
                        "temperature": self.temp,  # Adjust as needed
                        "max_tokens":self.max_tokens,
                        "top_p":self.top_p,
                        "frequency_penalty":self.frequency_penalty,
                        "presence_penalty":self.presence_penalty
                    }

                    client = OpenAI(
                        api_key=openai_api_key,
                        base_url=openai_api_base,
                    )


                    response = client.chat.completions.create(model=self.model_path,
                                                                messages=prompt,
                                                                temperature=self.temp,
                                                                max_tokens=3500,
                                                                top_p=self.top_p,
                                                                frequency_penalty=self.frequency_penalty,
                                                                presence_penalty=self.presence_penalty
                                                            )

                    # Send request to vLLM API
                    #response = requests.post("http://localhost:8000/v1/chat/completions", headers=headers, json=data)
                    
                    
                    resp = response.choices[0].message.content
                    print("resp:", resp)
                    if len(resp) > 0:
                        return resp, response
                    else:
                        print(f"Error for {video_id}: {response}")
                else:
                    params = SamplingParams(temperature=0.0, max_tokens=50000)
                    output = llm.generate(str(prompt[0]["content"]), params)
                    out = output[0].outputs[0].text
                    print("out:", out)
                    return out, output
            else:
                # gpt3 API call + response
                response = client.completions.create(model=self.model_name,
                prompt=prompt,
                temperature=self.temp,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty)
                return self.parse_gpt3_api_response(response)
        except openai.ServiceUnavailableError:
            print("Service unavailable error hit")
            time.sleep(20)
            return self.make_openai_api_call(prompt)
        # except openai.error.APIError: # Issue on their end, retry after 60 seconds
        #     print ("API error hit")
        #     time.sleep(60)
        #     return self.make_openai_api_call(prompt)
        except openai.RateLimitError:
            print("Rate limit error hit")
            time.sleep(60)
            return self.make_openai_api_call(prompt)

    def parse_gpt3_api_response(self, response):
        choices = response.choices
        return choices[0]["text"].strip(), response

    def parse_chatgpt_api_response(self, response):
        choices = response.choices
        main_response = choices[0].message
        main_response_message, main_response_role = main_response["content"], main_response["role"]
        # TODO: process "finish_reason" to check for "stop" or "length"
        return main_response_message, response

    def parse_ptsd_output_as_string(self, json_output):
        """
        Parses the PTSD subscale output as a raw string to extract severity scores.

        Args:
            json_output (str): The raw string output resembling a JSON structure.

        Returns:
            list: A list of severity scores [Re-experiencing, Avoidance, Dysphoria, Hyperarousal].
                If parsing fails, returns [1, 1, 1, 1] as a fallback.
        """
        try:
            # Define a dictionary to store the extracted scores
            scores = []

            # Use regular expressions to find each severity score
            for subscale in ["Re-experiencing", "Avoidance", "Dysphoria", "Hyperarousal"]:
                # Pattern to find the severity score for the subscale
                pattern = rf'"{subscale}":.*?"Severity Score":\s*(\d)'
                match = re.search(pattern, str(json_output), re.DOTALL)
                
                if match:
                    # Append the severity score as an integer
                    scores.append(int(match.group(1)))
                else:
                    # Append a fallback score if the subscale is missing
                    scores.append(1)

        except Exception as e:
            # Return fallback scores in case of an error
            return [1, 1, 1, 1]

        return scores

    def run_inference(self, prompt, video_id, llm=None):

        hashed_prompt = hashlib.sha256(str(prompt).encode("utf-8")).hexdigest()
        cache_key = (hashed_prompt, self.model_name, self.max_tokens, self.temp, self.top_p, self.frequency_penalty, self.presence_penalty)
        if cache_key in self.cached_responses:
            print(f"Using cached response")
            response_text = self.cached_responses[cache_key]['text']
            print(response_text)
        else:
            # print(f"Running {self.model_name}")
            print("making openai api call")
            response_text, response = self.make_openai_api_call(prompt, video_id, llm)

            #print("response text:", response_text)
            self.cached_responses[cache_key] = {'text': response_text, 'object': response}

        #print("resp:", response)

        #scores = self.parse_ptsd_output_as_string(response_text)
        scores = [1,1,1,1]
        #print("Scores:", scores)

        overall_score = (scores[0] + 1) * 5 + (scores[1] + 1) * 2 + (scores[2] + 1) * 8 + (scores[3] + 1) * 2
        #print("Overall score:", overall_score)

        tokenized_ids = self.tokenizer.encode(response_text, return_tensors='pt')  # Adjust based on vLLM API response format

        serialized_data = pickle.dumps({video_id: [tokenized_ids]})
        nonce = os.urandom(12)  # Generate a unique nonce for AES-GCM

        cipher = Cipher(algorithms.AES(self.encryption_key), modes.GCM(nonce), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(serialized_data) + encryptor.finalize()
        tag = encryptor.tag  # Store the authentication tag

        # Append encrypted data to the pickle file
        with open(self.PICKLE_NAME, "ab") as f:
            pickle.dump((self.encryption_salt, nonce, tag, encrypted_data), f)

        """serialized_scores = pickle.dumps({video_id: overall_score})
        nonce = os.urandom(12)  # Generate a new nonce for AES-GCM
        cipher = Cipher(algorithms.AES(self.encryption_key), modes.GCM(nonce), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_scores = encryptor.update(serialized_scores) + encryptor.finalize()
        tag = encryptor.tag  # Store the authentication tag"""

        if os.path.exists(self.PICKLE_NAME_SCORES):
            with open(self.PICKLE_NAME_SCORES, "rb") as f:
                data = pickle.load(f)

            # Add new key-value pair
            #data[video_id] = overall_score
        
        else:
            data = dict()
            #data[video_id] = overall_score

        with open(self.PICKLE_NAME_SCORES, "wb") as f:
            pickle.dump(data, f)

        print(f"Encrypted and saved tokenized data for {video_id}")
        with open(self.cache_path, 'wb') as handle:
            pickle.dump(self.cached_responses, handle)
        time.sleep(3)

        return response_text