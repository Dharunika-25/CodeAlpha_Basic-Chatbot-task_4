def chatbot():
    print("🤖 Simple Chatbot")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hello Dharuni! 👋")
        
        elif user_input == "how are you":
            print("Bot: I'm doing great! How about you?")
        
        elif user_input == "what is your name":
            print("Bot: I am a simple rule-based chatbot.")
        
        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day! 😊")
            break
        
        else:
            print("Bot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
