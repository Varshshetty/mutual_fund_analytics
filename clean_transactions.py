import pandas as pd

# Read file
df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("Original Shape:")
print(df.shape)

# Convert date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Check amount
invalid_amount = df[
    df["amount_inr"] <= 0
]

print("\nInvalid Amount Rows:")
print(len(invalid_amount))

# Check KYC values
print("\nKYC Status Values:")
print(df["kyc_status"].unique())

# Check transaction types
print("\nTransaction Types:")
print(df["transaction_type"].unique())

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("\nShape After Cleaning:")
print(df.shape)

print("\nSaved Successfully!")