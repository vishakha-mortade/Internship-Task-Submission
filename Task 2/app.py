import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="My Chatbot", layout="wide")
st.title("Multimodal AI Chatbot")

api_key = "YOUR_API_KEY_HERE"
genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-lite",
    system_instruction="Be helpful and talk like a normal person."
)

if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:
    st.header("Upload Image")
    img_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])
    if img_file:
        img = Image.open(img_file)
        st.image(img)

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_text = st.chat_input("Type your message here...")

if user_text:
    st.session_state.history.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    with st.chat_message("assistant"):
        inputs = [user_text]
        if img_file:
            inputs.append(img)
            
        try:
            response = model.generate_content(inputs, stream=True)
            
            output = ""
            box = st.empty()
            
            for chunk in response:
                output += chunk.text
                box.markdown(output)
            
            st.session_state.history.append({"role": "assistant", "content": output})
            
        except Exception as e:
            st.error("Error: " + str(e))