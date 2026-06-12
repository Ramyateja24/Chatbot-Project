print("Welcome to Rule-Based AI Chatbot")
print("Type 'exit' to stop chatting.")

while True:

    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello!")

    elif user == "how are you?":
        print("Bot: I am fine. Thank you!")

    elif user == "what is your name":
        print("Bot: My name is RuleBot.")

    elif user == "help":
        print("Bot: You can ask me simple questions.")

    elif user == "bye" or user == "exit":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")