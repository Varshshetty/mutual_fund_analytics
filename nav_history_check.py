import pandas as pd

nav = pd.read_csv("data/raw/02_nav_history.csv")

print("Columns:")
print(nav.columns.tolist())

print("\nShape:")
print(nav.shape)

print("\nHead:")
print(nav.head())