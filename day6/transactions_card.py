# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv("../data/transactions_card.csv")
df

# %%
df["dt_transaction"] = pd.to_datetime(df['dt_transaction'], format="%d/%m/%Y")
df

# %%
df["quotation_value"] = df.apply(lambda row : [row["value"] / row["quotation"] for i in range( row["quotation"] )], axis=1)
df


# %%
df_fatura = (df.explode("quotation_value")
             .drop(["value", "quotation"], axis=1))
df_fatura

# %%
df_fatura["months_add"] = df_fatura.groupby("transaction_id")["dt_transaction"].rank(method="first").astype(int)
df_fatura

# %%
def add_months(row):
    new_date = row["dt_transaction"] + pd.DateOffset(months = row["months_add"])
    return new_date

df_fatura["dt_quotation"] = (df_fatura.apply(add_months, axis=1)
                             .to_numpy()
                             .astype("datetime64[M]"))
df_fatura

# %%
df_fatura_mes = df_fatura.groupby(["client_id", "dt_quotation"])["quotation_value"].sum().reset_index()
df_fatura_mes