import pandas as pd
import sqlite3

csv_path = "data/raw/Medicare_Physician_Other_Practitioners_by_Provider_2023.csv"
db_path = "tt_cms_medicare.db"

import os
print("Current working folder:", os.getcwd())
print("DB full path:", os.path.abspath(db_path))

conn = sqlite3.connect(db_path)

chunksize = 50000
first_chunk = True

for i, chunk in enumerate(pd.read_csv(csv_path, chunksize=chunksize, low_memory=False)):
    print(f"Processing chunk {i + 1}")

    # 1. Standardize column names
    chunk.columns = chunk.columns.str.lower().str.strip()

    # 2. Remove duplicate rows
    chunk = chunk.drop_duplicates()

    # 3. Fill missing provider type
    if "rndrng_prvdr_type" in chunk.columns:
        chunk["rndrng_prvdr_type"] = chunk["rndrng_prvdr_type"].fillna("Unknown")

    # 4. Fill missing state
    if "rndrng_prvdr_state_abrvtn" in chunk.columns:
        chunk["rndrng_prvdr_state_abrvtn"] = chunk["rndrng_prvdr_state_abrvtn"].fillna("Unknown")

    # 5. Convert important numeric columns
    numeric_cols = [
        "tot_srvcs",
        "tot_mdcr_pymt_amt",
        "tot_sbmtd_chrg"
    ]

    for col in numeric_cols:
        if col in chunk.columns:
            chunk[col] = pd.to_numeric(chunk[col], errors="coerce")

    # 6. Remove rows missing key analytic values
    chunk = chunk.dropna(subset=["tot_srvcs", "tot_mdcr_pymt_amt", "tot_sbmtd_chrg"])

    # 7. Remove invalid negative values
    chunk = chunk[
        (chunk["tot_srvcs"] >= 0) &
        (chunk["tot_mdcr_pymt_amt"] >= 0) &
        (chunk["tot_sbmtd_chrg"] >= 0)
    ]

    # 8. Load cleaned chunk to SQLite
    chunk.to_sql(
        "medicare_provider_clean",
        conn,
        if_exists="replace" if first_chunk else "append",
        index=False
    )

    first_chunk = False

conn.close()

print("DONE! Clean data loaded to SQLite table: medicare_provider_clean")