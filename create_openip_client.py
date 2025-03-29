import os
from openai import AzureOpenAI

# Function to create OpenIP client
def create_openip_client():
        try:
            endpoint = "https://newsparser.openai.azure.com/"
            api_version = "2024-12-01-preview"
            subscription_key = os.getenv("AZURE_OPENAPI_KEY")

            # Creating AI client
            client = AzureOpenAI(
                api_version=api_version,
                azure_endpoint=endpoint,
                api_key=subscription_key,
            )
            return client
        except Exception as e:
            print(f"Error during creating AI client: {e}")
        return None