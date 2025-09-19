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

    text_output = [
        {
            "role": "system",
            "content": "You are a travel guide. Strictly dont answer anything outside this scope",
        },
        {
            "role": "user",
            "content": "Tell me about Shashank Dimri"
        }
    ]

    response = client.chat.completions.create(
        model = AZURE_DEPLOYMENT_NAME,
        messages = text_output
    )

    print(response.choices[0].message.content)

connect_llm()