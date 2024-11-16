import openai

# Set up your OpenAI API key
openai.api_key = 
def get_chatbot_response(user_input, conversation_history=[]):
    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Call the OpenAI API with the conversation history
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo" if you're using that model
        messages=conversation_history
    )

    # Get the assistant's reply and add it to the conversation history
    assistant_reply = response['choices'][0]['message']['content']
    conversation_history.append({"role": "assistant", "content": assistant_reply})

    return assistant_reply, conversation_history

# Start a conversation loop with the chatbot
conversation_history = [{"role": "system", "content": "You are a helpful assistant."}]
print("Chatbot: Hello! How can I help you today?")

while True:
    # Get user input
    user_input = input("You: ")

    # Break the loop if the user wants to end the chat
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    # Get the chatbot's response
    chatbot_reply, conversation_history = get_chatbot_response(user_input, conversation_history)
    
    # Print the chatbot's response
    print(f"Chatbot: {chatbot_reply}")
