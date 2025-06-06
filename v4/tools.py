from users import user_objects

# Define the custom tool
tools = [
    # {
    #     "type": "function",
    #     "function": {
    #         "name": "get_user_account_info",
    #         "description": "Retrieves the requested user's account information by netid.",
    #         "parameters": {
    #                 "type": "object",
    #                 "properties": {
    #                     "netid": {
    #                         "type": "string",
    #                         "description": "The netid of the user whose account information is being requested."
    #                     }
    #                 },
    #             "required": ["netid"]
    #         }
    #     }
    # },
    {
        "type": "function",
        "function": {
            "name": "provision_grouper_membership",
            "description": "Requests Grouper to synchronize a membership for a user in a group. All downstream systems will be updated.",
            "parameters": {
                    "type": "object",
                    "properties": {
                        "netid": {
                            "type": "string",
                            "description": "The netid of the user."
                        },
                        "groupid": {
                            "type": "string",
                            "description": "The groupid of the Grouper group being synchronized."
                        }
                    },
                "required": ["netid", "groupid"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "notify_sponsor_to_have_user_select_email_type",
            "description": "Notify the sponsor of eligible users to remind the user to select their preferred email type from the company portal: Google Workspace or Microsoft 365. A message can be provided to override the default",
            "parameters": {
                    "type": "object",
                    "properties": {
                        "netid": {
                            "type": "string",
                            "description": "The netid of the user who sponsor will be emailed."
                        },
                        "message": {
                            "type": "string",
                            "description": "The message to send to the user's sponsor."
                        }
                    },
                "required": ["netid"]
            }
        }
    }
]

# # Function to simulate tool execution
# def get_user_account_info(account_netid):
#     return user_objects.get(account_netid, {"error": "User not found"})
