from MCP_Server.Tools.rest import (
    fetch_table_contract,
    fetch_table_expenses,
    fetch_table_people,
    fetch_table_projects,
    fetch_table_timesheets,
)
from rapidfuzz import fuzz


def classify_content(message):
    # Load all clusters into dataframes
    tables = {
        "contracts": fetch_table_contract(),
        "expenses": fetch_table_expenses(),
        "people": fetch_table_people(),
        "projects": fetch_table_projects(),
        "timesheets": fetch_table_timesheets(),
    }

    best_score = -1
    best_cluster = None
    best_id = None
    best_endpoint = None

    for cluster_name, df in tables.items():   # ✅ unpack key + dataframe
        for _, row in df.iterrows():
            # Compare message with Example Intent String
            score = fuzz.token_sort_ratio(
                message.lower(), row["Example Intent String"].lower()
            )

            if score > best_score:
                best_score = score
                best_cluster = cluster_name
                best_id = row["ID"]
                best_endpoint = row["API Endpoint"]

    return {
        "cluster": best_cluster,
        "id": best_id,
        "endpoint": best_endpoint,
    }



# print(classify_content("List expense types."))

# Run python -m MCP_Server.Tools.classify_context from root folder Hackathon-AIS