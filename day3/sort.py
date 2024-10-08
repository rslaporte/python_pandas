# %%
import pandas as pd

# %%
df = pd.read_csv("../data/customers.csv", sep=";")
df

# %%
# Sorting values
df.sort_values(by=["Points", "Name"], ascending=[False, True]).tail(10)

# %%
# Drop duplicate command (you can drop by any column, so it can work like a filter)
df = (df.sort_values(by=["Points", "Name"], 
                     ascending=[False, True])
        .rename(columns={"Name" : "Nome", "Points" : "Pontos"}))
df