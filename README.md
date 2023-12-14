## Chat with Gemini Pro
This repo is a console app demo of Chatting with Gemini Pro, in Completion and Chat modes

## How to use
1. Clone this repo
2. Create an API key in Google AI Studio (https://makersuite.google.com/app/apikey)
3. Create a .env file:
   ```
   GEMINI_API_KEY=your_api_key
   ```
4. Install the requirements:
    ```
    pip install -r requirements.txt
    ```

5. Run the app:
   Use completion or chat modes. In chat mode, you can optionally pass the *--stream* argument to to get a more interactive experience.

    ```
    python app.py # completion mode

    python app.py # chat mode
    python app.py --stream # chat mode with streaming
    ```
    