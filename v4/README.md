Demonstrates: We are providing new "tools" that the LLM can call to try to fix the account issue it identifies. Our tools only "spy" and report on tool execution so we can see what tools/functions are called and the inputs the LLM provides.

The prompt gets updated slighty to ask the LLM to try to fix the issue. The RAG was updated with a some additional deal to aid it in tool choice...to help it realize that notifying the sponsor is an option vs just a group sync.

Note: We are going to initially, directly provide the account info to the model, like we did in v2, to save a conversational round trip and keep the code tighter.

```sh
/usr/local/bin/python /workspaces/mindstone-py/v4/main.py jtg59
/usr/local/bin/python /workspaces/mindstone-py/v4/main.py jtg69
/usr/local/bin/python /workspaces/mindstone-py/v4/main.py jtg79
```

Sample output:

```
$ /usr/local/bin/python /workspaces/mindstone-py/v4/main.py jtg59
netid: jtg59
Assistant response: The user's Active Directory account is disabled (`enabled`: False), which is why they are having issues with their account.
```

```
$ /usr/local/bin/python /workspaces/mindstone-py/v4/main.py jtg69
netid: jtg69
Assistant response: The user `jtg69` is in the `grouper:Students` group but not in the `grouper:email:Eligible` group, which is required to have email access. I will request Grouper to add the user to the `grouper:email:Eligible` group and provision the necessary Active Directory group.

Function call requested: provision_grouper_membership
Arguments: {'netid': 'jtg69', 'groupid': 'grouper:email:Eligible'}
```

```
$ /usr/local/bin/python /workspaces/mindstone-py/v4/main.py netid: jtg79
Assistant response: The user `jtg79` is in the "grouper:email:Eligible" group, which is necessary for email eligibility. However, there are no groups starting with "grouper:licenses:M365_A5_" or "grouper:licenses:GSuite_" indicating that the user hasn't selected their preferred email system via the employee portal. 

Let's notify the sponsor to remind the user to select their preferred email type.

Function call requested: notify_sponsor_to_have_user_select_email_type
Arguments: {'netid': 'jtg79'}
```
