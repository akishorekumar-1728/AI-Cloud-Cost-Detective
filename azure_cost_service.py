import os
import requests
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential

load_dotenv()

def get_azure_cost_data():

    try:

        tenant_id = os.getenv("AZURE_TENANT_ID")
        client_id = os.getenv("AZURE_CLIENT_ID")
        client_secret = os.getenv("AZURE_CLIENT_SECRET")
        subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")

        # Check variables
        if not all([
            tenant_id,
            client_id,
            client_secret,
            subscription_id
        ]):
            print("Azure environment variables missing")
            return None

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

        url = (
            f"https://management.azure.com/"
            f"subscriptions/{subscription_id}/"
            f"providers/Microsoft.CostManagement/query"
            f"?api-version=2023-03-01"
        )

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

        if response.status_code == 200:
            return response.json()

        print("Azure API Error:", response.text)
        return None

    except Exception as e:

        print("Azure Cost Fetch Error:", str(e))
        return None