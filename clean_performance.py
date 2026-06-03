import pandas as pd

# Read file
df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("Original Shape:")
print(df.shape)

# Convert return columns to numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Check for missing values
print("\nMissing Values:")
print(df[return_cols].isnull().sum())

# Find unusual return values
anomalies = df[
    (df["return_1yr_pct"] > 100) |
    (df["return_1yr_pct"] < -100)
]

print("\nAnomalies Found:")
print(len(anomalies))

# Check expense ratio
expense_issues = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Issues:")
print(len(expense_issues))

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("\nSaved Successfully!")