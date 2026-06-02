import pandas as pd

df = pd.read_csv(
    "data/raw/Medicare_Physician_Other_Practitioners_by_Provider_2023.csv",
    low_memory=False
)

print(df.head())
print(df.info())