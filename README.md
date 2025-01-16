## Ai-ify
Ai-Ify utilizes...
- Multiple hugging face libaries
- OpenAI to enlargen initial depiction
- Seamless UI utilizing Streamlit

This code does not include...
- HuggingFace token
- OpenAI key

## Introduction
This application combines advanced machine learning capabilities to generate text descriptions from images and recreate visuals based on those descriptions, effectively acting as an AI-powered "broken telephone." This tool is not only fun and engaging but also demonstrates practical applications of AI in image processing, content creation, and artistic expression.

## Overview
![image](https://github.com/user-attachments/assets/87e79fe7-fd5f-4ffd-84e8-2ce5342faf12)
This is the homepage. The middle has an upload panel allowing users to upload JPG, PNG, and JPEG images. Let's upload an image!

![image](https://github.com/user-attachments/assets/4b3fc92c-c300-41eb-b8f1-6efacfcf2082)
Here we uploaded a picture of Spiderman in the rain. Utilizing [BLIP Image Captioning Base](https://huggingface.co/Salesforce/blip-image-captioning-base) we can see that it depicts the picture as "spider and spider in the rain".

![image](https://github.com/user-attachments/assets/07fe0a0f-9eeb-4fd1-9b54-eabf7afdcfe5)
Finally, in the last stage of our pipeline we feed the previous scenario into [Stable Diffusion 3.5](https://huggingface.co/stabilityai/stable-diffusion-3.5-large), a text-to-image model. Here we can see it depicts the spider in the rain.

## Next Steps
- Integrate OpenAI's gpt-3.5-turbo I want to make the scenarios provided by BLIP longer, creating unique stories from the limited words 
- Utilize [Kan Bayashi Ljspeech](https://huggingface.co/espnet/kan-bayashi_ljspeech_vits), a text-to-speech model, to depict the scenario provided by the image-to-text or the story generator from OpenAI

## Credits
- [BLIP Image Captioning Base](https://huggingface.co/Salesforce/blip-image-captioning-base)
- [Stable Diffusion 3.5](https://huggingface.co/stabilityai/stable-diffusion-3.5-large)
- [Kan Bayashi Ljspeech](https://huggingface.co/espnet/kan-bayashi_ljspeech_vits)


## Try it for yourself!
1. Must have python3
2. Clone repository
```
git clone https://github.com/JacobJungg/Ai-Ify.git 
```
3. Install dependencies
```
pip install transformers streamlit pillow requests python-dotenv
```
4. Create an .env file in root directory and add the following unique tokens
```
HUGGINGFACE_API_TOKEN = 'hf_XXXXXXXX'
OPENAI_API_KEY = 'xxxxxxxxxxxxxxxx'
```
5. Run the frontend
```
streamlit run main.py
```
