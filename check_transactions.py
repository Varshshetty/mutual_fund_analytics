import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("Columns:")
print(df.columns.tolist())

print("\nShape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())