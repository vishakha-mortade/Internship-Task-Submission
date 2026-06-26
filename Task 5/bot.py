from textblob import TextBlob

def start_chatbot():
    print("Hi there! I'm a simple sentiment analysis bot. Type 'exit' when you want to leave.")
    
    responses = {
    "positive": "That's awesome to hear! Let me know if you need anything else.",
    "negative": "Oh no, I'm really sorry about that. Tell me what went wrong so I can fix it.",
    "neutral": "Got it. What should we look at next?"
}
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Bot: Goodbye! Have a great day.")
            break
            
      
        analysis = TextBlob(user_input)
        score = analysis.sentiment.polarity
        
   
        if score > 0.1:
            print(f"Bot: {responses['positive']}")
        elif score < -0.1:
            print(f"Bot: {responses['negative']}")
        else:
            print(f"Bot: {responses['neutral']}")
 
start_chatbot()