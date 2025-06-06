rag = """
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
1. When the identity lifecycle system determines that a user is eligible for email, it will add them to the "grouper:email:Eligible" Grouper group. Users MUST be in "grouper:email:Eligible" to have email.
2. If the user is in the "grouper:email:Eligible", this enables the user to choose which email system they want to be in the employee portal.
3. When the user chooses which email system they want to use via the employee portal, it adds them to a Grouper group that starts with "grouper:licenses:M365_A5_" for M365 or "grouper:licenses:GSuite_" for Google Workspace.
   A notifcation can be sent to the user's sponsor to remind them to select their preferred email type if they are eligible but have not yet made a choice.
4. Grouper provisions all "grouper:licenses:*" groups to Active Directory.
5. Grouper provisions any "grouper:licenses:M365_*" groups to Entra ID. These Entra ID groups have M365 license associated with them.
6. Grouper provisions the "grouper:licenses:Gsuite" group to Google. This Google Directory group has a license associated with it.
[/CONTEXT]
"""