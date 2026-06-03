# check_aum_columns.py

import pandas as pd

df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print(df.columns)
print(df.head())