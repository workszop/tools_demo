from PIL import Image
from gradio_client import Client

prompt = input('enter your image prompt:\n')

client = Client("ByteDance/SDXL-Lightning")
result = client.predict(
		prompt,	# str  in 'Enter your prompt (English)' Textbox component
		"4-Step",	# Literal['1-Step', '2-Step', '4-Step', '8-Step']  in 'Select inference steps' Dropdown component
		api_name="/generate_image"
)

print(result)
img = Image.open(result)
img.show()
