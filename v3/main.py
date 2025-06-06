import json
import requests
import sys
from rag import rag
from tools import tools, get_user_account_info

debug = False

# Define the model name
model_name = "ai/qwen2.5"
# model_name = "ai/qwen3"

# OpenAI API endpoint
url = "http://model-runner.docker.internal/engines/llama.cpp/v1/chat/completions"

# OpenAI API key
api_key = "your_openai_api_key"

if len(sys.argv) > 1:
    netid = sys.argv[1]
    print(f"netid: {netid}")
else:
    print("No netid provided.")
    sys.exit(1)


# Define the initial prompt
data = {
    "model": model_name,
    "messages": [
        {"role": "system", "content": f"You are an identity access management analyst that helps help desk staff quickly understand why a user does not have access to their email. Limit your response to the information provided in the context. Responses should be concise and to the point, preferably one sentence. Used this context to answer the user's question: {rag}"},
        {"role": "user", "content": f"Why might the user with netid `{netid}` be having issues with their account? Be as specific as possible about where the issue may lie."}
    ],
    "tools": tools
}

# Set headers
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

if debug:
    print(f"Request data: {data}")

# Send the request
response = requests.post(url, headers=headers, json=data)
response_data = response.json()

if debug:
    print(f"Response data: {response_data}")

# Properly extract tool calls based on Qwen's response format
choices = response_data.get("choices", [])
if choices:
    assistant_response = choices[0].get("message", {})
    tool_calls = assistant_response.get("tool_calls", [])

    for tool_call in tool_calls:
        function_info = tool_call.get("function", {})
        function_name = function_info.get("name")
        arguments = json.loads(function_info.get("arguments", "{}"))  # Ensuring valid JSON

        if function_name == "get_user_account_info":
            ai_determined_netid = arguments.get("netid") #
            if debug:
                print(f"AI determined netid: {ai_determined_netid}")
            account_info = get_user_account_info(ai_determined_netid)
            if debug:
                print(f"retrieved data: {account_info}")

            # Send tool execution result back (adjusting based on Qwen's response format)
            followup_data = {
                "model": model_name,
                "messages": [
                    {"role": "system", "content": f"You are an identity access management analyst that helps help desk staff quickly understand why a user does not have access to their email. Limit your response to the information provided in the context. Responses should be concise and to the point, preferably one sentence. Used this context to answer the user's question: {rag}"},
                    {"role": "user", "content": f"Why might the user with netid `{netid}` be having issues with their account? Be as specific as possible about where the issue may lie."},
                    {"role": "assistant", "content": "Let me check that for you..."},
                    {
                        "role": "tool",
                        "tool_call_id": tool_call["id"],
                        "name": "get_user_account_info",
                        "content": json.dumps(account_info)
                    }
                ]
            }

            if debug:
                print(f"follow up request: {followup_data}")

            followup_response = requests.post(url, headers=headers, json=followup_data)
            if debug:
                print(f"follow up request: {followup_response}")
            print(followup_response.json()['choices'][0]['message']['content'])
