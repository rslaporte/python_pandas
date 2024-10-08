# %%
import pandas as pd
import numpy as np

# %%
data = {
    "name": ["A", "B", "C", "D", "E"],
    "idade": [1, 30, 10, 45, np.nan],
    "renda": [np.nan, 3245, 357, 12321, np.nan]
}

df = pd.DataFrame(data)
df

# %%
df["idade"].isna().sum()

# %%
# All NaN in dataframe
df.isna().sum()

# %%
# % Of NaN in each column
df.isna().mean()

# %%
# Fill NA
df.fillna({
    "idade": df["idade"].mean(),
    "renda": df["renda"].mean()
})

# %
# Dropna
df.dropna(subset=["idade", "renda"], how='all')

# %%
df.dropna(axis=1, thresh=3)