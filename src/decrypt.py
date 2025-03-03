import pickle
import os
import getpass
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from transformers import AutoTokenizer

PICKLE_FILENAME = "/home/pkaliosis1/deepseek-ptsd/gpt4-depression-schema/out/expts/responses/qwen_w_reasoning_w_defs_wo_questions.pkl"

### **Function to Derive the Decryption Key**
def derive_decryption_key(salt, password):
    """
    Uses the provided salt to derive the encryption key for decryption.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend(),
    )
    return kdf.derive(password.encode())

if not os.path.exists(PICKLE_FILENAME):
    print("No encrypted data found!")
    exit()

decrypted_data = {}

# **Open the Pickle File and Read the First Entry for Salt**
with open(PICKLE_FILENAME, "rb") as f:
    try:
        # Read the first encrypted entry to extract the salt
        salt, nonce, tag, encrypted_data = pickle.load(f)

        # Prompt for the password ONCE and derive the key
        password = getpass.getpass("Enter the password for decryption: ")
        decryption_key = derive_decryption_key(salt, password)

        # Process the first entry
        cipher = Cipher(algorithms.AES(decryption_key), modes.GCM(nonce, tag), backend=default_backend())
        decryptor = cipher.decryptor()
        serialized_data = decryptor.update(encrypted_data) + decryptor.finalize()
        decrypted_data.update(pickle.loads(serialized_data))

        # Read the remaining entries using the same key
        while True:
            try:
                salt, nonce, tag, encrypted_data = pickle.load(f)  # Read without salt
                cipher = Cipher(algorithms.AES(decryption_key), modes.GCM(nonce, tag), backend=default_backend())
                decryptor = cipher.decryptor()
                serialized_data = decryptor.update(encrypted_data) + decryptor.finalize()
                decrypted_data.update(pickle.loads(serialized_data))
            except EOFError:
                break  # Stop reading when reaching the end of file

    except EOFError:
        print("Encrypted file is empty or corrupted!")
        exit()

print("Decryption successful! Loaded tokenized data.")

scores = decrypted_data.values()
print(scores)
# **Print First Few Results for Verification**
for k, v in list(decrypted_data.items())[:5]:
    print(f"🔹 {k}: {v}")