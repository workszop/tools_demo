# you need to have ollama (ollama.ai) and tinyllama model on your machine

from openai import OpenAI

client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)

prompt = input('how can I help you?\n')

response = client.chat.completions.create(
  model="tinyllama",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt},
  ]
)
print(response.choices[0].message.content)
