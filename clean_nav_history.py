import pandas as pd

# Read NAV file
nav = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:")
print(nav.shape)

# Convert date column to datetime
nav["date"] = pd.to_datetime(nav["date"])

# Remove duplicate rows
nav = nav.drop_duplicates()

# Sort by fund and date
nav = nav.sort_values(
    ["amfi_code", "date"]
)

print("\nShape After Cleaning:")
print(nav.shape)

# Save cleaned file
nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("\nFile Saved Successfully!")