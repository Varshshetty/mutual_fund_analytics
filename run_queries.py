import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

query = """
SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()