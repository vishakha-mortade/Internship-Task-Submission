import google.generativeai as genai
import os

os.environ["GOOGLE_API_KEY"] = "MY_API_KEY"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

print("🔍 Checking available models for your key...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f" AVAILABLE: {m.name}")
except Exception as e:
    print(f" Error models: {e}")