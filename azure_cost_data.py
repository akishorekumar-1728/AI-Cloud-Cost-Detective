import os
import requests
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential

load_dotenv()

tenant_id = os.getenv("AZURE_TENANT_ID")
client_id = os.getenv("AZURE_CLIENT_ID")
client_secret = os.getenv("AZURE_CLIENT_SECRET")
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")

credential = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)

token = credential.get_token(
    "https://management.azure.com/.default"
)

headers = {
    "Authorization": f"Bearer {token.token}",
    "Content-Type": "application/json"
}

url = f"https://management.azure.com/subscriptions/{subscription_id}/providers/Microsoft.CostManagement/query?api-version=2023-03-01"

body = {
    "type": "ActualCost",
    "timeframe": "MonthToDate",
    "dataset": {
        "granularity": "Daily",
        "aggregation": {
            "totalCost": {
                "name": "Cost",
                "function": "Sum"
            }
        }
    }
}

response = requests.post(
    url,
    headers=headers,
    json=body
)

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("✅ Cost Data Retrieved")
    print(response.json())
else:
    print("❌ Failed")
    print(response.text)