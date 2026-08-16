import pandas as pd

# Original dataset
INPUT_FILE = "data/raw/Medicare_Physician_Other_Practitioners_by_Provider_2023.csv"

# Output sample file
OUTPUT_FILE = "data/raw/cms_medicare_sample_2023.csv"


def create_sample():
    print("Loading dataset...")
    df = pd.read_csv(INPUT_FILE, low_memory=False)

    print("Standardizing columns...")
    df.columns = df.columns.str.lower().str.strip()

    print("Dropping duplicates...")
    df = df.drop_duplicates()

    print("Creating stratified sample by provider type...")

    # taking maximum 100 rows for each provider_type
    sample_df = (
        df.groupby("rndrng_prvdr_type", group_keys=False)
        .apply(lambda x: x.sample(n=min(len(x), 100), random_state=42))
        .reset_index(drop=True)
    )

    print(f"Sample size: {len(sample_df)} rows")

    print("Saving sample file...")
    sample_df.to_csv(OUTPUT_FILE, index=False)

    print("Done! Sample saved to:", OUTPUT_FILE)


if __name__ == "__main__":
    create_sample()