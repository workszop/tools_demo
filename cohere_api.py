# pip install cohere

import cohere
# from cohere.responses.chat import StreamEvent
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("COHERE_KEY")

co = cohere.Client(api_key)

prompt = input('how can I help you?\n')

stream = co.chat_stream(message=prompt)

for event in stream:
    if event.event_type == 'text-generation':
        print(event.text, end='')
