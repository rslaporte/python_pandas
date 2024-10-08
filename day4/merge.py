# %%
import pandas as pd

# %%
data_users = {
    "id": [1,2,3,4],
    "name": ["A", "B", "C", "D"],
    "age": [30,40,20,25]
}

df_users = pd.DataFrame(data_users)
df_users

# %%

data_transactions = {
    "user_id": [1,1,1,2,3,3,3,4,4,7],
    "value": [20, 10, 5, 5.9, 30, 15, 30, 8, 9,5],
    "qtProdutos": [2, 3, 1, 5, 1, 1, 2, 2, 10, 12]
}

df_transactions = pd.DataFrame(data_transactions)
df_transactions

# %%
df_transactions.merge(df_users, 
                      how="left", 
                      left_on='user_id',
                      right_on="id")

# %%
df_transactions.merge(df_users, 
                      how="right", 
                      left_on='user_id',
                      right_on="id")

# %%
df_merge = df_transactions.merge(df_users, 
                      how="left", 
                      left_on='user_id',
                      right_on="id")

df_merge[df_merge["name"].isna()]