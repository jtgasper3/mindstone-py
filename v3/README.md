Demonstrates: We provide the netid in chat and the AI Agent looks up the account details using LLM's tools functionality. This also uses a formal message array prompt setup.

```sh
/usr/local/bin/python /workspaces/mindstone-py/v3/main.py jtg59
/usr/local/bin/python /workspaces/mindstone-py/v3/main.py jtg69
/usr/local/bin/python /workspaces/mindstone-py/v3/main.py jtg79
```

Sample output:

```
$ /usr/local/bin/python /workspaces/mindstone-py/v3/main.py jtg59
netid: jtg59
The issue might lie in Active Directory, as the account for netid `jtg59` is disabled. Email services are not allowed for disabled accounts.
```

```
$ /usr/local/bin/python /workspaces/mindstone-py/v3/main.py jtg69
netid: jtg69
User `jtg69` has an active account in Active Directory but is not a member of any "grouper:licenses:*" groups in Grouper, which are required for M365 or Google Workspace email provisioning.
```

```
$ /usr/local/bin/python /workspaces/mindstone-py/v3/main.py jtg79
netid: jtg79
User `jtg79` has an enabled account in Active Directory and is in the "grouper:email:Eligible" group, which should allow them to choose their email system. However, they are not in any "grouper:licenses:M365_A5_" or "grouper:licenses:GSuite_" group, meaning their mailbox hasn't been provisioned.
```