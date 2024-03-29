from PIL import Image
from gradio_client import Client

prompt = input('enter your image prompt:\n')

client = Client("radames/Real-Time-Text-to-Image-SDXL-Lightning")
result = client.predict(
		prompt,	# str in 'parameter_5' Textbox component
		0,	# float (numeric value between 0 and 12013012031030)in'Seed' Slider component
		api_name="/predict_1"
)
print(result)
img = Image.open(result)
img.show()
