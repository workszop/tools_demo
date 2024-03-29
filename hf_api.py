import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv('HF_KEY')

def query(payload, model_id, api_token):
	headers = {"Authorization": f"Bearer {api_token}"}
	API_URL = f"https://api-inference.huggingface.co/models/{model_id}"
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

model_id = "distilbert-base-uncased"
api_token = "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"
data = query("The goal of life is [MASK].", model_id, api_token)
print(data)
