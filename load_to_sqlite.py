import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

print("Database Created!")

# NAV
nav = pd.read_csv("data/processed/nav_history_clean.csv")
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
print("NAV Loaded")

# Performance
performance = pd.read_csv("data/processed/scheme_performance_clean.csv")
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)
print("Performance Loaded")

# Transactions
transactions = pd.read_csv("data/processed/investor_transactions_clean.csv")
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
print("Transactions Loaded")

print("\nAll Data Loaded Successfully!")