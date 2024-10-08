# %%
import pandas as pd
import datetime as dt

# %%
df = pd.read_excel("../data/transactions.xlsx")
df

# %%
condition = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df[condition]

# %%
# Group by + aggr
df_summary = df.groupby("IdCustomer")["Points"].sum()
df_summary

# %%
df_summary.reset_index()

# %%
(df.groupby(["IdCustomer"])
    .agg({"Points" : "sum", 
          "UUID" : "count",
          "DtTransaction" : "max"
        })
    .rename(columns={
            "Points": "Valor",
             "UUID" : "Frequência",
             "DtTransaction" : "Última data"
            })
    .reset_index()
)

# %%
def days_till_last_purchase(date):
    diff = dt.datetime.now() - date.max()
    return diff.days

(df.groupby(["IdCustomer"])
    .agg({"Points" : "sum", 
          "UUID" : "count",
          "DtTransaction" : ["max", days_till_last_purchase]
        })
    .rename(columns={
            "Points": "Valor",
             "UUID" : "Frequência",
             "DtTransaction" : "Última data"
            })
    .reset_index()
)
