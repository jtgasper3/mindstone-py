Demonstrates: We are providing new "tools" that the LLM can call to try to fix the account issue it identifies. Our tools only "spy" and report on tool execution so we can see what tools/functions are called and the inputs the LLM provides.

The prompt gets updated slighty to ask the LLM to try to fix the issue. The RAG was updated with a some additional deal to aid it in tool choice...to help it realize that notifying the sponsor is an option vs just a group sync.

Note: We are going to initially, directly provide the account info to the model, like we did in v2, to save a conversational round trip and keep the code tighter.

```sh
/usr/local/bin/python /workspaces/mindstone-py/v4/main.py jtg59
/usr/local/bin/python /workspaces/mindstone-py/v4/main.py jtg69
/usr/local/bin/python /workspaces/mindstone-py/v4/main.py jtg79
```
