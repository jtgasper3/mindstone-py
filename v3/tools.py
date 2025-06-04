from users import user_objects

# Define the custom tool
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_user_account_info",
            "description": "Retrieves the requested user's account information by netid.",
            "parameters": {
                    "type": "object",
                    "properties": {
                        "netid": {
                            "type": "string",
                            "description": "The netid of the user whose account information is being requested."
                        }
                    },
                "required": ["netid"]
            }
        }
    }
]

# Function to simulate tool execution
def get_user_account_info(account_netid):
    return user_objects.get(account_netid, {"error": "User not found"})
