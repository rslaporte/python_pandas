# %%
import pandas as pd

# %%
df_customer = pd.read_csv("../data/customers.csv", sep=";")
df_customer

#
# %%
df_transactions = pd.read_excel("../data/transactions.xlsx")
df_transactions

# %%
df_transactions_products = pd.read_parquet("../data/transactions_cart.parquet")
df_transactions_products

# %%
df_join = (df_transactions.merge(df_customer,
                                how="inner",
                                left_on="IdCustomer",
                                right_on="UUID",
                                suffixes=["_transactions", "_customer"])
                          .merge(df_transactions_products,
                                how="inner",
                                left_on="UUID_transactions",
                                right_on="IdTransaction",
                                suffixes=["_transactions", "_transaction_products"])
                                )

df_join