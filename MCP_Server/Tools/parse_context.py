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

# Mapping of placeholder -> keywords to look for in the text
PLACEHOLDER_KEYWORDS = {
    "id": ["timesheet", "time", "expense", "contract", "project", "person"],
    "attachmentId": ["attachment"],
    "projectId": ["project", "proj"],
    "taskId": ["task"],
    "clause_id": ["clause"],
    "mod_number": ["mod", "modification"],
    "exp_budget_id": ["exp_budget", "expense budget"],
    "exp_plan_id": ["exp_plan", "expense plan"],
    "expense_type_id": ["expense_type", "expense type"],
    "wage_determination_id": ["wage_determination", "wage determination"],
    "benefitsValueId": ["benefitsValue", "benefits value"],
    "personAccrualPlanId": ["accrual_plan", "accrual plan"],
    "rateId": ["rate"],
    "owning_org_id": ["organization", "owning organization"],
    "budget_snapshot_id": ["budget_snapshot", "budget snapshot"]
}


def map_numbers_to_placeholders(input_text: str, endpoint_template: str) -> dict:
    """
    Map numbers from input_text to all placeholders in endpoint_template
    based on keywords, and return a dict like {id: 5, attachmentId: 10}.
    """
    lowered_text = input_text.lower()
    placeholders = re.findall(r"\{(\w+)\}", endpoint_template)
    entities = {}

    # Extract numbers with preceding words
    matches = re.findall(r"([\w\s]+?)\s+(\d+)", lowered_text)

    used_numbers = set()

    for ph in placeholders:
        keywords = PLACEHOLDER_KEYWORDS.get(ph, [])
        assigned = False
        for word, num in matches:
            num_int = int(num)
            if num_int in used_numbers:
                continue
            for kw in keywords:
                if kw in word:
                    entities[ph] = num_int
                    used_numbers.add(num_int)
                    assigned = True
                    break
            if assigned:
                break
        # Fallback: assign first unused number if keyword not found
        if not assigned:
            for _, num in matches:
                num_int = int(num)
                if num_int not in used_numbers:
                    entities[ph] = num_int
                    used_numbers.add(num_int)
                    break

    return entities




# After defining map_numbers_to_placeholders, add this helper
def fill_endpoint(endpoint_template: str, placeholder_mapping: dict) -> str:
    """
    Replace all placeholders in endpoint_template with actual numbers
    from placeholder_mapping and return the filled endpoint.
    """
    filled = endpoint_template
    for ph, val in placeholder_mapping.items():
        filled = filled.replace(f"{{{ph}}}", str(val))
    return filled


def extract_int_entities(text: str) -> list[int]:
    """Extract all integer tokens from text (positive integers)."""
    matches = re.findall(r"\b\d+\b", text)
    return [int(m) for m in matches]

def match(entities, endpoint):
    count = 0
    for i in endpoint:
        if i == '{':
            count += 1
    return entities == count

def parse_context(input_text):
    if _keyword_pattern.search(input_text) == None:
        return None
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

inputs = [
    "List all people",
    "Get all alerts for project 5.",
    "Get attachment 10 for timesheet 5.",
    "Get the list of locations for project ID 2 in timesheet ID 1",
    "Show locations for task ID 9 in timesheet ID 3.",
    "Show labor categories for task ID 7 in timesheet ID 2.",
    "List all labor categories for project 2 under timesheet 10.",
    "Fetch attachment 2 in timesheet 1.",
    "Retrieve the details of budget snapshot 10 from project 1.",
    "Show expense budget ID 2 in project ID 3.",
    "Get expense plan 5 for project 2.",
    "Retrieve details for expense type 8 of project 2.",
    "Get attachment 10 for expense 5.",
    "Get clause 2 for contract 4.",
    "Get mod 1 for contract 5.",
    "Get detail 3 for expense 7.",
    "Get wage determination 3 for contract 2.",
    "Get master contracts for owning organization 7.",
    "Get rate 5 for person 2.",
    "Get benefits value 3 for person 4.",
    "Get accrual plan 2 for person 6.",
    "Get attachment 8 for person 3."
    
]


for txt in inputs:
    endpoint_info = parse_context(txt)
    matched_endpoint = endpoint_info[2]

    # Get mapping of placeholder → number
    placeholder_mapping = map_numbers_to_placeholders(txt, matched_endpoint)

    # Fill actual endpoint
    filled_endpoint = fill_endpoint(matched_endpoint, placeholder_mapping)

    print("Original Input:", txt)
    print("Matched Endpoint:", matched_endpoint)
    print("Mapping:", placeholder_mapping)
    print("Filled Endpoint:", filled_endpoint)
    print("-----")


res = parse_context("Get the list of locations for a specific project within a particular timesheet, using the timesheet ID 1 and project ID 2")
print("Result:", res)