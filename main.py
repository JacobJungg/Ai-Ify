import streamlit as st
from image_to_text import img2text
from text_to_image import text2image
from PIL import Image

def main():
    st.set_page_config(page_title="AI-ify", page_icon="🖼️")
    st.title("AI-ify")
    st.header("Upload an image to AI-ify it!")

    # File uploader for the image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Read the uploaded image into a PIL Image object
        image = Image.open(uploaded_file)

        # Generate text from the uploaded image
        with st.spinner("Generating text from image..."):
            generated_text = img2text(image)

        st.subheader("Generated Text from Image")
        st.write(generated_text)

        # Generate a new image based on the text
        with st.spinner("Generating a new image from text..."):
            generated_image = text2image(generated_text)

        if generated_image:
            st.subheader("Generated Image")
            st.image(generated_image, caption="Generated Image", use_column_width=True)
        else:
            st.error("Failed to generate an image. Please check the logs.")

if __name__ == "__main__":
    main()