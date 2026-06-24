import pandas as pd
import os

os.makedirs(
    "data/processed",
    exist_ok=True
)

nav = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code","date"]
)

nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

os.makedirs(
    "C:/Users/soham/MutualFundProject/data/processed",
    exist_ok=True
)

nav.to_csv(
    "C:/Users/soham/MutualFundProject/data/processed/nav_history_clean.csv",
    index=False
)

print("File saved successfully")

txn = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/08_investor_transactions.csv")

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.upper()
)

mapping = {
"SIP":"SIP",
"SYSTEMATIC INVESTMENT PLAN":"SIP",
"LUMPSUM":"LUMPSUM",
"REDEMPTION":"REDEMPTION"
}

txn["transaction_type"] = txn[
"transaction_type"
].replace(mapping)

txn = txn[
txn["amount_inr"] > 0
]

txn["transaction_date"] = pd.to_datetime(
txn["transaction_date"]
)

valid = [
"VERIFIED",
"PENDING",
"REJECTED"
]

invalid_kyc = txn[
~txn["kyc_status"].isin(valid)
]

txn.to_csv(
"data/processed/investor_transactions_clean.csv",
index=False
)

print("File Saved Succesfully!")

perf = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/07_scheme_performance.csv")

perf["return_1yr_pct"] = pd.to_numeric(
perf["return_1yr_pct"],
errors="coerce"
)

invalid = perf[
perf["return_1yr_pct"].isna()
]

anomalies = perf[
(perf["expense_ratio_pct"] < 0.1)
|
(perf["expense_ratio_pct"] > 2.5)
]

perf.to_csv(
"data/processed/scheme_performance_clean.csv",
index=False
)

print("File Saved Succesfully!")

fund = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/01_fund_master.csv")

fund = fund.drop_duplicates()

fund.columns = fund.columns.str.lower().str.strip()

fund.to_csv(
    "data/processed/fund_master_clean.csv",
    index=False
)
print("File Saved Succesfully!")

aum = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/03_aum_by_fund_house.csv")

aum = aum.drop_duplicates()

aum = aum.fillna(0)

aum.to_csv(
    "data/processed/aum_by_fund_house_clean.csv",
    index=False
)
print("File Saved Succesfully!")

sip = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/04_monthly_sip_inflows.csv")

sip = sip.drop_duplicates()

sip = sip.fillna(0)

sip.to_csv(
    "data/processed/monthly_sip_inflows_clean.csv",
    index=False
)
print("File Saved Succesfully!")

cat = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/05_category_inflows.csv")

cat = cat.drop_duplicates()

cat = cat.fillna(0)

cat.to_csv(
    "data/processed/category_inflows_clean.csv",
    index=False
)
print("File Saved Succesfully!")

folio = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/06_industry_folio_count.csv")

folio = folio.drop_duplicates()

folio = folio.fillna(0)

folio.to_csv(
    "data/processed/industry_folio_count_clean.csv",
    index=False
)
print("File Saved Succesfully!")

hold = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/09_portfolio_holdings.csv")

hold = hold.drop_duplicates()

hold = hold.fillna("Unknown")

hold.to_csv(
    "data/processed/portfolio_holdings_clean.csv",
    index=False
)
print("File Saved Succesfully!")

bench = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/10_benchmark_indices.csv")

bench = bench.drop_duplicates()

bench.to_csv(
    "data/processed/benchmark_indices_clean.csv",
    index=False
)
print("File Saved Succesfullt!")