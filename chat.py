import google.generativeai as genai
from dotenv import load_dotenv
import os
import argparse  # Import argparse

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
# Set the API key
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Set up command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--stream", action="store_true", help="Enable streaming mode")
args = parser.parse_args()
stream = args.stream

# Start the chat loop
while True:
    # Get the user's input
    user_input = input("User: ")

    # Check if user wants to print the history
    if user_input.lower() == "history":
        print("\n\n--------------\n\n")
        print(chat.history)
        print("\n\n--------------\n\n")
        continue
    # Check if the user wants to exit
    if user_input.lower() == "exit":
        break

    # Generate text
    response = chat.send_message(user_input, stream=stream)
    if stream:
        for chunk in response:
            print(chunk.text)
    else:
        # Print the generated text
        print("Gemini:", response.candidates[0].content.parts[0].text)

# Print a goodbye message
print("Goodbye!")
