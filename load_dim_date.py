import pandas as pd
import sqlite3

# Read NAV data
df = pd.read_csv("data/processed/nav_history_clean.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Get unique dates
dates = pd.DataFrame({
    "full_date": sorted(df["date"].unique())
})

# Create date attributes
dates["year"] = dates["full_date"].dt.year
dates["quarter"] = dates["full_date"].dt.quarter
dates["month"] = dates["full_date"].dt.month
dates["month_name"] = dates["full_date"].dt.month_name()
dates["day"] = dates["full_date"].dt.day
dates["weekday"] = dates["full_date"].dt.day_name()

# Load into SQLite
conn = sqlite3.connect("bluestock_mf.db")

dates.to_sql(
    "dim_date",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print(f"Loaded {len(dates)} dates into dim_date")