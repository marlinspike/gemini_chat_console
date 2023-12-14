import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

api_key = api_key = os.getenv("GEMINI_API_KEY")
# Set the API key
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

# Start the chat loop
while True:
    # Get the user's input
    user_input = input("User: ")

    # Check if the user wants to exit
    if user_input.lower() == "exit":
        break

    # Generate text
    response = model.generate_content(user_input)

    # Print the generated text
    print("Gemini:", response.candidates[0].content.parts[0].text)

# Print a goodbye message
print("Goodbye!")