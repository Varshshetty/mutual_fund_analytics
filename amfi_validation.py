import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_in_nav = master_codes - nav_codes
extra_in_nav = nav_codes - master_codes

print("\nFund Master Codes:")
print(len(master_codes))

print("\nNAV History Codes:")
print(len(nav_codes))

print("\nMissing In NAV:")
print(len(missing_in_nav))

print("\nExtra In NAV:")
print(len(extra_in_nav))

if len(missing_in_nav) > 0:
    print("\nMissing Codes:")
    print(list(missing_in_nav)[:20])

if len(extra_in_nav) > 0:
    print("\nExtra Codes:")
    print(list(extra_in_nav)[:20])