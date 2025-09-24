from rest import fetch_table_contract, fetch_table_expenses, fetch_table_people, fetch_table_projects, fetch_table_timesheets
import numpy as np

def default_embeddings(client, AZURE_DEPLOYMENT):
    df_contract = fetch_table_contract()
    df_expenses = fetch_table_expenses()
    df_people = fetch_table_people()
    df_projects = fetch_table_projects()
    df_timesheets = fetch_table_timesheets()

    dfs = [df_contract, df_expenses, df_people, df_projects, df_timesheets]

    for df in dfs:
        contexts = df["Intents"]
        full_vecs = []
        for intent in contexts:
            intent_vec = client.embeddings.create(
                            model = AZURE_DEPLOYMENT,
                            input = intent
                        )
            full_vecs.append(intent_vec.data[0].embedding)
        df["Embeddings"] = full_vecs

    # Store each value(each controller's dataframe) from dfs into local file system (make a new folder and store json file)
    # format: id endpoint intent embedding
    return dfs