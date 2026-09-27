import pandas as pd

FILE_PATH = "data/enwiki_namespace_0_00052.parquet"


def load_data():
    return pd.read_parquet(FILE_PATH)


def search_articles(df, query, limit=10):
    query = query.lower().strip()

    if not query:
        return df.head(0)

    name_matches = df[
        df["name"].fillna("").str.lower().str.contains(query, regex=False)
    ]

    if len(name_matches) < limit:
        description_matches = df[
            df["description"]
            .fillna("")
            .str.lower()
            .str.contains(query, regex=False)
        ]

        results = pd.concat(
            [name_matches, description_matches]
        ).drop_duplicates(subset=["identifier"])

    else:
        results = name_matches

    return results.head(limit)


if __name__ == "__main__":
    df = load_data()

    print("Dataset loaded!")
    print("Rows:", len(df))

    results = search_articles(df, "Cataract")

    print("\nSearch results:")
    print(results[["name", "description"]].to_string(index=False))