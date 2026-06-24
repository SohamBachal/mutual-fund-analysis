from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
"sqlite:///bluestock_mf.db"
)

df = pd.read_csv("C:/Users/soham/MutualFundProject/data/processed/nav_history_clean.csv")

df.to_sql(
"fact_nav",
engine,
if_exists="replace",
index=False
)
print("Source Rows:", len(df))

count = pd.read_sql(
    "SELECT COUNT(*) as cnt FROM fact_nav",
    engine
)

print(count)

df1 = pd.read_csv("C:/Users/soham/MutualFundProject/data/processed/investor_transactions_clean.csv")

df1.to_sql(
"fact_transactions",
engine,
if_exists="replace",
index=False
)
print("Source Rows:", len(df1))

count = pd.read_sql(
    "SELECT COUNT(*) as cnt FROM fact_transactions",
    engine
)

print(count)

df2 = pd.read_csv("C:/Users/soham/MutualFundProject/data/processed/scheme_performance_clean.csv")

df2.to_sql(
"fact_performance",
engine,
if_exists="replace",
index=False
)
print("Source Rows:", len(df2))

count = pd.read_sql(
    "SELECT COUNT(*) as cnt FROM fact_performance",
    engine
)

print(count)