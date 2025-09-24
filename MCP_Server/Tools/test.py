from data import save_all_data
from parse_context import parse_context
from openai import OpenAI
import os

AZURE_KEY = os.getenv("EMBEDDING_KEY")
AZURE_ENDPOINT = os.getenv("EMBEDDING_ENDPOINT")

client = OpenAI(
    api_key = AZURE_KEY,
    base_url = AZURE_ENDPOINT
)

# print(parse_context(client = client, input = "Tell me about expense 42"))

from default_embeddings import default_embeddings

df = default_embeddings(client = client, AZURE_DEPLOYMENT = "text-embedding-3-large")

# save_all_data(df)
