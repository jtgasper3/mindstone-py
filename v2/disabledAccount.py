from rag import rag
from call_openai_api import call_openai_api

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
    
    prompt = rag.format(userObject)

    # Call the API
    response = call_openai_api(prompt)
    print("Response:", response)

if __name__ == "__main__":
    main()
