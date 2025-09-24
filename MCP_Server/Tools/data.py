import os
import pandas as pd

def save_all_data(dfs, folder="Data"):
    # JSON
    # Excel
    os.makedirs(folder, exist_ok=True)

    names = ["contracts", "expenses", "people", "projects", "timesheets"]

    all_data = {}
    for df, name in zip(dfs, names):
        df_to_save = df.copy()
        df_to_save["Embeddings"] = df_to_save["Embeddings"].apply(lambda x: list(map(float, x)))
        all_data[name] = df_to_save.to_dict(orient="records")
# json
    json_path = os.path.join(folder, "data.json")
    import json
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=2)
    print(f"Saved")
# excel
    excel_path = os.path.join(folder, "data.xlsx")
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        for df, name in zip(dfs, names):
            df_to_save = df.copy()
            df_to_save["Embeddings"] = df_to_save["Embeddings"].apply(lambda x: str(list(map(float, x))))
            df_to_save.to_excel(writer, sheet_name=name, index=False)
    print(f"Saved")


#  function is called in test.py