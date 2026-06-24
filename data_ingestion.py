import pandas as pd

# For 01_Fund_Master.csv

df = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/01_fund_master.csv")
print(df)
df.shape
df.head()
df.describe()
df.info()
df.isnull().count()
df.dtypes

# For 02_nav_history.csv

df1 = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/02_nav_history.csv")
print(df1)
df1.shape
df1.head()
df1.describe()
df1.info()
df1.isnull().count()
df1.dtypes

# For 03_aum_by_fund_house

df2 = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/03_aum_by_fund_house.csv")
print(df2)
df2.shape
df2.head()
df2.describe()
df2.info()
df2.isnull().count()
df2.dtypes

# For 04_monthly_sip_inflows

df3 = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/04_monthly_sip_inflows.csv")
print(df3)
df3.shape
df3.head()
df3.describe()
df3.info()
df3.isnull().count()
df3.dtypes

# For 05_category_inflows

df4 = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/05_category_inflows.csv")
print(df4)
df4.shape
df4.head()
df4.describe()
df4.info()
df4.isnull().count()
df4.dtypes

# For 06_industry_folio_count

df5 = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/06_industry_folio_count.csv")
print(df5)
df5.shape
df5.head()
df5.describe()
df5.info()
df5.isnull().count()
df5.dtypes

#For 07_scheme_performance

df6 = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/07_scheme_performance.csv")
print(df6)
df6.shape
df6.head()
df6.describe()
df6.info()
df6.isnull().count()
df6.dtypes

#For 08_investor_transactions

df7 = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/08_investor_transactions.csv")
print(df7)
df7.shape
df7.head()
df7.describe()
df7.info()
df7.isnull().count()
df7.dtypes

# For 09_portfolio_holdings

df8 = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/09_portfolio_holdings.csv")
print(df8)
df8.shape
df8.head()
df8.describe()
df8.info()
df8.isnull().count()
df8.dtypes

# For 10_benchmark_indices

df9 = pd.read_csv("C:/Users/soham/MutualFundProject/data/raw/10_benchmark_indices.csv")
print(df9)
df9.shape
df9.head()
df9.describe()
df9.info()
df9.isnull().count()
df9.dtypes        