Demonstrates: Run through some various account states and see what the AI Agent determines.

```sh
/usr/local/bin/python /workspaces/mindstone-py/v2/disabledAccount.py
/usr/local/bin/python /workspaces/mindstone-py/v2/notEligible.py
/usr/local/bin/python /workspaces/mindstone-py/v2/noLicensingGroup.py
```

Sample output:

```
$ /usr/local/bin/python /workspaces/mindstone-py/v2/disabledAccount.py
Response: The user's account might be having issues because the Active Directory account is disabled (`enabled: false`). This prevents the user from logging in and accessing email services.
```

```
$ /usr/local/bin/python /workspaces/mindstone-py/v2/notEligible.py
Response: The user might be having issues because they are not a member of the "grouper:email:Eligible" group in Grouper, which is required to enable email service access.
```

```
$ /usr/local/bin/python /workspaces/mindstone-py/v2/noLicensingGroup.py
Response: The user might be having issues because they are not a member of any "grouper:licenses:*" group, which is required for provisioning M365 or Google Workspace licenses.
```