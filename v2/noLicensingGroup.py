from rag import rag
from call_openai_api import call_openai_api

def main():
    # Example prompt
    userObject = """
    { 
      ActiveDirectory: {
        accountExpires: null,
        enabled: true,
        givenName: "Bob",
        groups: ["All Users", "Students", "Entra ID Syncd"],
        mail: "bob.anderson@example.org",
        samAccountName: "banderson",
        sn: "Anderson",
        userPrincipalName: "bob.anderson@example.org"
      },
      Grouper: {
        groups: ["grouper:email:Eligible", "grouper:Students"]
      }
    }
    """
    
    prompt = rag + userObject + "[/QUESTION]"

    # Call the API
    response = call_openai_api(prompt)
    print("Response:", response)

if __name__ == "__main__":
    main()
