import pandas as pd

FILE_PATH = "data/enwiki_namespace_0_00052.parquet"

df = pd.read_parquet(FILE_PATH)

print("Number of rows:", len(df))
print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 articles:")
print(df[["name", "description"]].head())