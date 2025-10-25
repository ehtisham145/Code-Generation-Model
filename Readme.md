This project is a chatbot that generates code using Google AI Studio’s Generative AI API. The chatbot takes a user’s prompt (e.g., “Write a Python function for sorting”) and returns ready-to-use code.This is actually a Cod e Generation Model developed by Ehtisham

Setup Steps:

Install dependencies using pip install -r requirements.txt.

Create a .env file and add your GOOGLE_AI_API_KEY.

Run the chatbot using python app.py or your main file.

Streamlit is used for front ends tasks

How It Works:

The chatbot sends the user’s prompt to Google AI Studio.

The API generates code based on the prompt.

The chatbot displays the generated code to the user.

Important Notes:

Never share or commit your API key.

Add error handling for empty prompts and failed requests.

Keep the temperature low for accurate results.

Log API usage and monitor cost limits.