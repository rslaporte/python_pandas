# %%
import pandas as pd

# %%
df = pd.read_excel("../data/transactions.xlsx")
df

# %%
# Get the last transaction from each IdCustomer
# Using the sort_values + drop_duplicates for drop every non desirable line
df_last = (df.sort_values(by='DtTransaction', ascending=False)
      .drop_duplicates(subset=['IdCustomer']))
df_last

#%%
## Counting unique values on a column
df['IdCustomer'].nunique()

#%%
#Verifying if everything works well
condition1 = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
condition2 = df_last["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df[condition1].iloc[-1]["DtTransaction"] == df_last[condition2]["DtTransaction"]

