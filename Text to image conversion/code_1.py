import google.generativeai as genai
from PIL import Image
import io

# Set your API key
genai.api_key = 'YOUR_API_KEY'

# Define the text prompt
text_prompt = "A beautiful sunset over the mountains"

# Generate the image
response = genai.generate_image(prompt=text_prompt, model="gemini-pro-vision")

# Convert the response to an image
image_data = response['image']
image = Image.open(io.BytesIO(image_data))

# Save or display the image
image.save("generated_image.png")
image.show()
