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

openai_api_key = "EMPTY"
openai_api_base = f"http://localhost:8000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

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
        self.tokenizer = tokenizer
        self.cached_responses = self.load_cache_if_exists()
        

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

    def make_openai_api_call(self, prompt, video_id):

        try:
            if self.model_name in ['gpt-3.5-turbo', 'gpt-4', 'gpt-4-1106-preview', 'gpt-4-0613']:
                response = client.chat.completions.create(model=self.model_name,
                messages=prompt,
                temperature=self.temp,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty)
                return self.parse_chatgpt_api_response(response)
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

                response = client.chat.completions.create(model=f"/home/pkaliosis1/pretrained/{self.model_name}",
                                                            messages=prompt,
                                                            temperature=self.temp,
                                                            max_tokens=self.max_tokens,
                                                            top_p=self.top_p,
                                                            frequency_penalty=self.frequency_penalty,
                                                            presence_penalty=self.presence_penalty
                                                        )

                # Send request to vLLM API
                #response = requests.post("http://localhost:8000/v1/chat/completions", headers=headers, json=data)
                
                
                resp = response.choices[0].message.content
                if len(resp) > 0:
                    return resp, response
                else:
                    print(f"Error for {video_id}: {response.text}")
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

    def run_inference(self, prompt, video_id):

        hashed_prompt = hashlib.sha256(str(prompt).encode("utf-8")).hexdigest()
        cache_key = (hashed_prompt, self.model_name, self.max_tokens, self.temp, self.top_p, self.frequency_penalty, self.presence_penalty)
        if cache_key in self.cached_responses:
            print(f"Using cached response")
            response_text = self.cached_responses[cache_key]['text']
        else:
            # print(f"Running {self.model_name}")
            response_text, response = self.make_openai_api_call(prompt, video_id)
            self.cached_responses[cache_key] = {'text': response_text, 'object': response}

        print(type(response_text))

        scores = self.parse_ptsd_output_as_string(response_text)
        print("Scores:", scores)

        overall_score = (scores[0] + 1) * 5 + (scores[1] + 1) * 2 + (scores[2] + 1) * 8 + (scores[3] + 1) * 2
        print("Overall score:", overall_score)

        tokenized_ids = self.tokenizer(response_text, return_tensors='pt')  # Adjust based on vLLM API response format

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
            data[video_id] = overall_score
        
        else:
            data = dict()
            data[video_id] = overall_score

        with open(self.PICKLE_NAME_SCORES, "wb") as f:
            pickle.dump(data, f)

        print(f"Encrypted and saved tokenized data for {video_id}")
        """with open(self.cache_path, 'wb') as handle:
            pickle.dump(self.cached_responses, handle)
        time.sleep(5)"""

        return response_text