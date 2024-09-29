import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyCvjajPWNVg7A7A4HBlvgl3ooLSu5ZBuy0")

model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text, image_date, prompt):
    response = model.generate_content([input_text,image_date[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no file was uploaded")
    
st.set_page_config(page_title="Diya's Invoice Generator")
st.sidebar.header("RoboBill")
st.sidebar.write("Made by Diya Bajoria")
st.sidebar.write("Powered by google gemini AI")
st.header("RoboBill")
st.subheader("Made by Diya Bajoria")
st.subheader("Manage your expenses with RoboBill")
input = st.text_input("What do you want me to do?",key="input")
uploaded_File = st.file_uploader("Choose an image",type=["jpg","jpeg","png"])
image =''
if uploaded_File is not None:
    image = Image.open(uploaded_File)
    st.image(image,caption="Voila! Uploaded Image",use_column_width=True)

ssumbit = st.button("Let's Go!")

input_promt = """
You are an expert in reading invoices. We are going to upload an image of an invoice
and you will have to answer any type of questions that the user asks you.
You have to great the user first. Make sure to keep the fonts uniform and give the items list
in a point-wise format.
At the end, make sure to repeat the name of our app "RoboBill" and ask the user to use it again.
"""

if ssumbit:
    image_data= input_image_details(uploaded_File)
    response= get_gemini_response(input_promt, image_data,input)
    st.subheader("Here's  what you need to know!")
    st.write(response)
