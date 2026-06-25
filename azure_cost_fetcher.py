import os
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential

load_dotenv()

TENANT_ID = os.getenv("AZURE_TENANT_ID")
CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")

try:
    credential = ClientSecretCredential(
        tenant_id=TENANT_ID,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )

    token = credential.get_token("https://management.azure.com/.default")

    print("✅ Azure Authentication Successful")
    print("Token received successfully")

except Exception as e:
    print("❌ Authentication Failed")
    print(e)