import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

def get_llm(model_name="models/gemini-2.5-flash"):
    if not API_KEY:
        raise ValueError(" GEMINI_API_KEY not found in environment variables.")

    genai.configure(api_key=API_KEY)

    return genai.GenerativeModel(model_name)
