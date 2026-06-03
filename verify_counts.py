import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

tables = [
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum",
    "dim_fund",
    "dim_date"
]

for table in tables:
    count = pd.read_sql(
        f"SELECT COUNT(*) AS rows FROM {table}",
        conn
    )

    print(f"\n{table}")
    print(count)

conn.close()