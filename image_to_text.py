from transformers import pipeline

# Load the image-to-text pipeline
image_to_text_pipeline = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

def img2text(image_path):
    """
    Extracts text from an image using Salesforce's BLIP model.
    """
    # Generate text from image
    text = image_to_text_pipeline(image_path)
    print("Generated Text from Image:", text[0]["generated_text"])
    return text[0]["generated_text"]
