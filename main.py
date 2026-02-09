# UI based on Streamlit for translating text using Gemini AI
import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Set Gemini API key
genai.configure(api_key=api_key)

# Supported Languages
languages = [
    "English","Urdu","China","Arabic","Spanish","French","German","Italian","Russian","Hindi","Bengali","Japanese","Korean","Turkish","Vietnamese","Polish","Dutch","Greek","Swedish","Czech","Hungarian",
]

# Streamlit UI
st.set_page_config(page_title="Translator by Farooq", layout="centered")
st.title("🤖 AI Translator")
st.write("Created by **Farooq Ahmed** 🪢 Translate your English text into various languages using Gemini AI.")

text = st.text_area("Enter English text to translate:", height=150)
lang = st.selectbox("Select target language:", languages)
btn = st.button("Translate")

if btn and text:
    try:
        model = genai.GenerativeModel('google/gemma-3-27b-it:free')
        prompt = f"Translate the following text to {lang}:\n\n{text}"
        response = model.generate_content(prompt)
        st.success(f"✅ Translated to {lang}:")
        st.markdown(f"**{response.text}**")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
