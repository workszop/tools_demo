import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
api_key =os.getenv('ANTHROPIC_KEY')

client = anthropic.Anthropic(api_key=api_key)

prompt = input('how can I help you?\n')

message = client.messages.create(
    model='claude-3-haiku-20240307',
    max_tokens=1024,
    messages=[
        {'role': 'user', 'content': prompt}
    ]
)

print(message.content[0].text)
