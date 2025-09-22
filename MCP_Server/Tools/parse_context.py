import re
from MCP_Server.Tools.classify_context import classify_content

def extract_entity_id(message: str):
    """
    Extract a numeric ID or code from the message if present.
    Example: "Get expense 123" -> "123"
             "Tell me about project P001" -> "P001"
    """
    # First try: find numbers (like expense ID 123)
    num_match = re.search(r"\b\d+\b", message)
    if num_match:
        return num_match.group(0)

    # Second try: alphanumeric IDs (like P001, T45, etc.)
    code_match = re.search(r"\b[A-Za-z]\w+\b", message)
    if code_match:
        return code_match.group(0)

    return None


def parse_context(message: str):
    # Step 1: classify intent
    classified = classify_content(message)
    intent_id = classified["id"]
    cluster = classified["cluster"]
    endpoint_template = classified["endpoint"]

    # Step 2: extract entity id (different from intent id!)
    entity_id = extract_entity_id(message)

    # Step 3: if endpoint has {id}, replace it
    if "{id}" in endpoint_template and entity_id:
        final_endpoint = endpoint_template.replace("{id}", str(entity_id))
    else:
        final_endpoint = endpoint_template

    return {
        "cluster": cluster,
        "intent_id": intent_id,    # from classify_context
        "entity_id": entity_id,    # extracted from message
        "endpoint": final_endpoint,
    }


# print(parse_context("Tell me about expense 42"))
# print(parse_context("List expense types."))
# print(parse_context("Show project P001 details"))
