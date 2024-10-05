# %%
import pandas as pd

# %%
df = pd.read_csv("../data/customers.csv", sep=";")
df

# %%
df.dtypes

# %%
df["Points"].astype(str)

# %%
df["Points_double"] = df["Points"] * 2

# %%
df[["Points", "Points_double"]].astype(float)