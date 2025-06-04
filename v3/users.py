user_objects = {}
user_objects['jtg59'] = {
    "ActiveDirectory": {
        "accountExpires": None,
        "enabled": False,
        "givenName": "Bob",
        "groups": ["All Users", "Students", "M365_A5_Student", "Entra ID Syncd"],
        "mail": "bob.anderson@example.org",
        "samAccountName": "banderson",
        "sn": "Anderson",
        "userPrincipalName": "bob.anderson@example.org"
    },
    "Grouper": {
        "groups": ["grouper:email:Eligible", "grouper:licenses:M365_A5_Student"]
    }
}

user_objects['jtg69'] = {
    "ActiveDirectory": {
        "accountExpires": None,
        "enabled": True,
        "givenName": "Bob",
        "groups": ["All Users", "Students", "Entra ID Syncd"],
        "mail": "bob.anderson@example.org",
        "samAccountName": "banderson",
        "sn": "Anderson",
        "userPrincipalName": "bob.anderson@example.org"
    },
    "Grouper": {
        "groups": ["grouper:Students"]
    }
}

user_objects['jtg79'] = {
    "ActiveDirectory": {
        "accountExpires": None,
        "enabled": True,
        "givenName": "Bob",
        "groups": ["All Users", "Students", "Entra ID Syncd"],
        "mail": "bob.anderson@example.org",
        "samAccountName": "banderson",
        "sn": "Anderson",
        "userPrincipalName": "bob.anderson@example.org"
    },
    "Grouper": {
        "groups": ["grouper:email:Eligible", "grouper:Students"]
    }
}
