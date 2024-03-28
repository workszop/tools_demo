import os
import openai
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_KEY"))

prompt = input('how can I help you?\n')

completion = client.chat.completions.create(
    model='gpt-3.5-turbo',
    temperature=0.7,
    max_tokens=500,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ],
    stream=True,
)

print("Response: ")
for event in completion:
    if event.choices:
        content = event.choices[0].delta.content
        print(content, end="", flush=True)
