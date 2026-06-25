import os
from dotenv import load_dotenv

load_dotenv()

print("TENANT =", repr(os.getenv("AZURE_TENANT_ID")))
print("CLIENT =", repr(os.getenv("AZURE_CLIENT_ID")))
print("SECRET =", repr(os.getenv("AZURE_CLIENT_SECRET")))
print("SUB =", repr(os.getenv("AZURE_SUBSCRIPTION_ID")))