from translator_logic import process_message

def start_chat():
    print("Multilingual Bot Active (Type 'exit' to stop) ")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
            
        bot_reply = process_message(user_input)
        print(f"Bot: {bot_reply}")

if __name__ == "__main__":
    start_chat()