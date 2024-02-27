import pandas as pd

sheet_id = '1CQg5iu--hRVxFSxusixd20uv3esse4r4lLERumzHXbQ'

df = pd.read_excel(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

print(df)
