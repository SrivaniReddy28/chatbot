import random

# Define responses for different types of user inputs
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!"],
    "goodbye": ["Goodbye!", "See you later!", "Have a great day!"],
    "thanks": ["You're welcome!", "No problem!", "My pleasure!"],
    "about_bot": ["I'm a chatbot designed to assist you.", "I'm here to help you with any questions!"],
    "default": ["That's interesting!", "Tell me more!", "I'm not sure I understand."],
    "mesmerizing": ["Imagine a world where everything is possible...", 
                    "Close your eyes and visualize your dreams...",
                    "Feel the magic of the unknown..."],
}

# Function to generate a response based on user input
def get_response(user_input, prev_responses):
    user_input = user_input.lower()

    if any(greeting in user_input for greeting in ["hello", "hi", "hey"]) and "greeting" not in prev_responses:
        return random.choice(responses["greeting"])

    elif any(bye_word in user_input for bye_word in ["bye", "goodbye"]) and "goodbye" not in prev_responses:
        return random.choice(responses["goodbye"])

    elif "thanks" in user_input and "thanks" not in prev_responses:
        return random.choice(responses["thanks"])

    elif ("about you" in user_input or "yourself" in user_input) and "about_bot" not in prev_responses:
        return random.choice(responses["about_bot"])

    elif ("mesmerize" in user_input or "magic" in user_input) and "mesmerizing" not in prev_responses:
        return random.choice(responses["mesmerizing"])

    else:
        return random.choice(responses["default"])

# Interactive chat loop
print("Welcome! I'm your mesmerizing chatbot. Ask me anything or say goodbye to exit.")

previous_responses = []

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print(get_response(user_input, previous_responses))
        break
    else:
        response = get_response(user_input, previous_responses)
        previous_responses.append(response)
        print("Chatbot:", response)
