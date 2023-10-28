import json
import requests

# Define the ChatGPT API endpoint and token
CHATGPT_API_ENDPOINT = "https://api.openai.com/v1/engines/davinci/completions"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"  # Replace with your actual API key

def lambda_handler(event, context):
    # Extract user input from the Lambda event
    user_input = event.get("userInput", "")

    # Prepare the headers for the ChatGPT API request
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    # Define the payload for the ChatGPT API request
    payload = {
        "prompt": user_input,
        "max_tokens": 150  # You can adjust this value as needed
    }

    # Make the API request to ChatGPT
    response = requests.post(CHATGPT_API_ENDPOINT, headers=headers, data=json.dumps(payload))

    # Extract the generated text from the API response
    response_data = response.json()
    generated_text = response_data.get("choices", [{}])[0].get("text", "").strip()

    # Return the generated text as the Lambda function's response
    return {
        "statusCode": 200,
        "body": json.dumps({
            "response": generated_text
        })
    }

