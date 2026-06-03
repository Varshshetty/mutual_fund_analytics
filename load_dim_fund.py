import pandas as pd
import sqlite3

# Read performance data
df = pd.read_csv("data/processed/scheme_performance_clean.csv")

# Create dimension table
dim_fund = df[
    ["amfi_code", "scheme_name", "fund_house", "category", "plan"]
].drop_duplicates()

# Connect to database
conn = sqlite3.connect("bluestock_mf.db")

# Remove old data
conn.execute("DELETE FROM dim_fund")

# Insert new data
dim_fund.to_sql(
    "dim_fund",
    conn,
    if_exists="append",
    index=False
)

conn.commit()
conn.close()

print(f"Loaded {len(dim_fund)} funds into dim_fund")
