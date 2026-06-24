import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(data)

nav_df = pd.DataFrame(data['data'])

print(nav_df.head())

nav_df.to_csv(
    "C:/Users/soham/MutualFundProject/data/raw/nav_125497.csv",
    index=False
)

scheme_codes = [
    119551,
    120503,
    118632,
    119092,
    120841
]

for code in scheme_codes:

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    file_path = f"data/raw/{code}.csv"

    nav_df.to_csv(file_path, index=False)

    print(f"Saved: {file_path}")
    
fund_master = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/01_fund_master.csv")

print(fund_master.head())

print(fund_master.columns)

print(fund_master["fund_house"].unique())

print(fund_master["category"].unique())

print(fund_master["sub_category"].unique())

print(fund_master["risk_category"].unique())

print(fund_master["fund_house"].value_counts())

print(fund_master["category"].value_counts())

print(fund_master["risk_category"].value_counts())




print(fund_master["amfi_code"].head())

print(fund_master["amfi_code"].nunique())

print(
    fund_master[
        ["amfi_code", "scheme_name"]
    ].head(10)
)



nav_history = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/02_nav_history.csv")

print(fund_master.columns)
print(nav_history.columns)

master_codes = set(fund_master["amfi_code"])

nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("Missing Codes:")
print(missing_codes)

print("Total Missing Codes:", len(missing_codes))