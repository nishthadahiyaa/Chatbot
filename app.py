from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv
import logging

# Load environment variables from the .env file
load_dotenv()

# Set the OpenAI API key from the .env file
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize the Flask app
app = Flask(__name__)

# Enable debug mode
app.config['DEBUG'] = True

# Set up logging for the app
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Log the incoming request
        app.logger.info(f"Received message: {request.data}")

        # Get the user message from the JSON body of the POST request
        data = request.get_json()  # This properly decodes the incoming JSON request
        message = data.get('msg')  
        if not message:
            return jsonify({"error": "No message provided"}), 400

        # Make the API call to OpenAI using the new interface (GPT-3.5 or GPT-4)
        response = openai.completions.create(
            model="gpt-3.5-turbo",  # Specify model, can change to gpt-4
            prompt=message,  # User's input as the prompt
            max_tokens=150  # Limit the response length
        )

        # Extract the response from OpenAI
        bot_reply = response['choices'][0]['text']
        return jsonify({"response": bot_reply})

    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
