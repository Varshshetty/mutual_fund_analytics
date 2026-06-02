import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

schemes = {
    "HDFC": 125497,
    "SBI": 119551,
    "ICICI": 120503,
    "NIPPON": 118632,
    "AXIS": 119092,
    "KOTAK": 120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        filename = f"data/raw/{name}_nav.csv"

        nav_df.to_csv(filename, index=False)

        print(f"Saved {filename}")

    else:
        print(f"Failed for {name}")