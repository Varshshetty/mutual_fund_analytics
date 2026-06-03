import pandas as pd
from sqlalchemy import create_engine

# Read raw AUM file
df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Connect database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load table
df.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print(f"Loaded {len(df)} rows into fact_aum")