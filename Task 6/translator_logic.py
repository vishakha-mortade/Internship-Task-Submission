from googletrans import Translator
from config import CULTURAL_GREETINGS

translator = Translator()

def process_message(user_text):
    
    detection = translator.detect(user_text)
    user_lang = detection.lang
    
    
    if user_text.lower() in ['hello', 'hi', 'hola', 'नमस्ते', 'bonjour']:
        return CULTURAL_GREETINGS.get(user_lang, CULTURAL_GREETINGS['en'])

    
    english_text = translator.translate(user_text, dest='en').text
    
    
    if "price" in english_text.lower() or "cost" in english_text.lower():
        response = "Our services are free for students."
    elif "name" in english_text.lower():
        response = "I am your Multilingual Assistant."
    else:
        response = "Oh Great! Let me look into that for you."

    
    final_response = translator.translate(response, dest=user_lang).text
    return final_response