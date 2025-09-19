import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

AZURE_ENDPOINT = os.getenv("OPENAI_ENDPOINT")  
AZURE_KEY = os.getenv("OPENAI_KEY")  
AZURE_DEPLOYMENT_NAME = os.getenv("OPENAI_DEPLOYMENT_NAME")
AZURE_API_VERSION = os.getenv("OPENAI_API_VERSION")

def connect_llm():
    client = AzureOpenAI(
        api_key = AZURE_KEY,
        azure_endpoint = AZURE_ENDPOINT,
        api_version = AZURE_API_VERSION
    )
    return client, AZURE_DEPLOYMENT_NAME