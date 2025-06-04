import json
import requests

# Define the model name
model_name = "ai/qwen2.5"
# model_name = "ai/qwen3"

# OpenAI API endpoint
url = "http://model-runner.docker.internal/engines/llama.cpp/v1/chat/completions"

# Replace with your OpenAI API key
api_key = "your-api-key"


def call_openai_api(prompt):    
    # Request headers
    headers = {
        "Content-Type": "application/json",
        # "Authorization": f"Bearer {api_key}"
    }
    
    # Request body
    data = {
        "model": model_name,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7
    }
    
    try:
        # Make the POST request
        response = requests.post(url, headers=headers, json=data)
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse and return the response
        result = response.json()
        return result['choices'][0]['message']['content']
    
    except requests.exceptions.RequestException as e:
        return f"Error making request: {str(e)}"
    except (KeyError, json.JSONDecodeError) as e:
        return f"Error parsing response: {str(e)}"