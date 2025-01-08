import requests
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def text2speech(message):
    """
    Converts the provided message to speech and saves it as an audio file.
    """
    payload = {"inputs": message}

    response = requests.post(API_URL, headers=headers, json=payload)
    with open('audio.flac', 'wb') as file:
        file.write(response.content)
