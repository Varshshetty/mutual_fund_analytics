import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

query = """
SELECT
    fund_house,
    ROUND(AVG(return_1yr_pct),2) AS avg_return
FROM fact_performance
GROUP BY fund_house
ORDER BY avg_return DESC;
"""

result = conn.execute(query).fetchall()

for row in result:
    print(row)

conn.close()