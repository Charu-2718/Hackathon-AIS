import os
from dotenv import load_dotenv
import numpy as np
import json
import re
from openai import OpenAI

load_dotenv()

AZURE_KEY = os.getenv("EMBEDDING_KEY")
AZURE_ENDPOINT = os.getenv("EMBEDDING_ENDPOINT")
AZURE_DEPLOYMENT = os.getenv("EMBEDDING_DEPLOYMENT")
JSON_PATH = os.getenv("JSON_EMBEDDINGS_STORE")

client = OpenAI(
    api_key = AZURE_KEY,
    base_url = AZURE_ENDPOINT
)

def extract_int_entities(text: str) -> list[int]:
    """Extract all integer tokens from text (positive integers)."""
    #########################################
    # Match the parameter and extracted entity (have to input parameters here as well and then extract the entity first)
    #########################################
    matches = re.findall(r"\b\d+\b", text)
    return [int(m) for m in matches]

def match(entities, endpoint):
    count = 0
    for i in endpoint:
        if i == '{':
            count += 1
    return entities == count

def parse_context(input_text):
    entities_count = len(extract_int_entities(input_text))
    resp = client.embeddings.create(
        model = AZURE_DEPLOYMENT,
        input = input_text
    )
    embedding = resp.data[0].embedding
    query_vec = np.array(embedding, dtype=float)

    def cosine_similarity(a, b):
        denom = np.linalg.norm(a) * np.linalg.norm(b)
        if denom == 0:
            return 0.0
        return np.dot(a, b) / denom

    # load stored embeddings
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    max_similarity = -1.0
    max_endpoint = None
    max_id = None
    best_api_endpoint = None

    for endpoint, items in data.items():
        #print("Checking endpoint:", endpoint)
        for each in items:
            api_ep = each.get("API Endpoint")
            if match(entities_count, api_ep) == False:
                continue
            stored_emb = each.get("Embeddings")
            if stored_emb is None:
                continue
            stored_vec = np.array(stored_emb, dtype = float)
            sim = cosine_similarity(query_vec, stored_vec)
            # debug print
            #print(f" → {api_ep}: similarity = {sim}")
            if sim > max_similarity:
                max_similarity = sim
                max_endpoint = endpoint
                max_id = each.get("ID")
                best_api_endpoint = api_ep

    # you can print or return
    #print("Best match:", max_endpoint, max_id, best_api_endpoint, "with sim:", max_similarity)
    return max_endpoint, max_id, best_api_endpoint

# example usage
# res = parse_context("Provide the list of of all contract  manager")
# print("Result:", res)

res = parse_context("Get the list of locations for a specific project within a particular timesheet, using the timesheet ID 1 and project ID 2")
print("Result:", res)