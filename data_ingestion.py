import pandas as pd
import os

folder = "data/raw"

files = os.listdir(folder)

for file in files:
    if file.endswith(".csv"):

        path = os.path.join(folder, file)

        print("\n" + "="*50)
        print(f"FILE: {file}")
        print("="*50)

        df = pd.read_csv(path)

        print("Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())
        print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nColumns:")
print(df.columns.tolist())