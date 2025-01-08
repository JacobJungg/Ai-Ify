import requests
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def text2image(prompt):
    """
    Generates an image based on the provided text prompt using Stable Diffusion.
    """
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        print("Image generated successfully!")
        return response.content
    else:
        print(f"Error: {response.status_code}, {response.json()}")
        return None
