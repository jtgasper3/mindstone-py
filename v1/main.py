import json
import requests

# Define the model name
model_name = "ai/qwen2.5"
# model_name = "ai/qwen3"

# OpenAI API endpoint
url = "http://model-runner.docker.internal/engines/llama.cpp/v1/chat/completions"

# Replace with your OpenAI API key
api_key = "your-api-key"

rag = """
[SYSTEM]
You are an access management analyst that helps help desk staff quickly understand why a user does not have access to their email. Limit your response to the information provided in the context. Responses should be concise and to the point, preferably one sentence.
[/SYSTEM]

[CONTEXT 1]
General knowledge:
- Grouper is a group management system that allows users to create and manage groups. It supports nested groups and set based operations intersection and minus for calculating group membership.
- Grouper Groups can also be created through loader jobs that source data from relation databases or ldap directories.
- Grouper can provisions groups to active directory, Google Workspace, and Microsoft 365.
- Entra ID Sync will provisioner users aand groups from Active Directory to Entra ID. It then adds users to the "Entra ID Syncd" AD and Entra ID groups when the sync is successful 
- M365 email licensing is provisioned by Grouper and its associated groups being published to Entra ID.
[/CONTEXT 1]

[CONTEXT 2]
Email provisioning requirements:
- We create mailboxes in either Google Workspace (aka Gmail) or Microsoft 365 (i.e. M365).
- Because both M365 and Google Workspace authenticate with Active Directory credentials, the user must have an enabled account in Active Directory to login.

Email provisioning flow:
1.  When the identity system determines that a user is eligible for email, it will add them to the "grouper:email:Eligible" Grouper group. This enables the user to choose which email system they want to be in the employee portal. If this membership isn't present, email is deprovisioned.
2. When the user chooses which email system they want to be in the employee portal, it adds them to group that starts with "grouper:licenses:M365_A5_" for M365 or "grouper:licenses:GSuite_" for Google Workspace.
3. Grouper provisions all "grouper:licenses:*" groups to Active Directory.
4. Grouper provisions any "grouper:licenses:M365_" groups to Entra ID. These Entra ID groups have M365 license associated with them.
5. Grouper provisions the "grouper:licenses:Gsuite" group to Google. This Google Directory group has a license associated with it.
[/CONTEXT]

[QUESTION]
Given this json object about a user. Why might the user be having issues with their account?
"""

def call_openai_api(prompt, api_key):    
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

def main():
    # Example prompt
    userObject = """
    { 
      ActiveDirectory: {
        accountExpires: null,
        enabled: false,
        givenName: "Bob",
        groups: ["All Users", "Students", "M365_A5_Student", "Entra ID Syncd"],
        mail: "bob.anderson@example.org",
        samAccountName: "banderson",
        sn: "Anderson",
        userPrincipalName: "bob.anderson@example.org"
      },
      Grouper: {
        groups: ["grouper:email:Eligible", "grouper:licenses:M365_A5_Student"]
      }
    }
    """
    
    prompt = rag + userObject + "\n[/QUESTION]"

    print("Prompt:", prompt)

    # Call the API
    response = call_openai_api(prompt, api_key)
    print("Response:", response)

if __name__ == "__main__":
    main()
