import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv() # loading all the environment variables
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt,image):
    model=genai.GenerativeModel('gemini-1.5-flash-8b-exp-0827')
    response=model.generate_content([input_prompt,image[0]])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

##initialize our streamlit app

#st.set_page_config(page_title="HealthyHer")

#st.header("HealthyHer")

# Path to the AI-generated image
ai_image_path = "/Users/humeraron/Downloads/HealthyHer.jpeg"  # Update this path to your actual image name
if os.path.exists(ai_image_path):
    ai_image = Image.open(ai_image_path)
    st.image(ai_image, caption="AI-Generated Image", use_column_width=True)
else:
    st.write("AI-generated image not found. Please check the path.")

#input=st.text_input("Input Prompt: ",key="input")
#File Uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Is It Healthy Or Not ?")

input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, provide the details of every food items with the calorie intake
               in below format

               1. What is the food item?
               2. How many calories does it have?
               3. Is it healthy or not?
"""

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data)
    st.header("The Response is")
    st.write(response)