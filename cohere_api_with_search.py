# pip install cohere

import cohere
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("COHERE_KEY")

prompt = input('how can I help you?\n')

co = cohere.Client(api_key=api_key)

response = co.chat(
  model="command",
  message=prompt,
  connectors=[{"id": "web-search"}])

print(response.text)
