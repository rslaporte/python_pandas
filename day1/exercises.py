# %% 
import pandas as pd

# %%
#Exercise 1
data = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
data_series = pd.Series(data)

print(data_series.mean())
print(data_series.std())
print(data_series.max())

# %%
#Exercise 2
data = {
    "nome": ['Téo', 'Nah', "Napoleão"],
    "idade": [31, 32, 14]
}

data_df = pd.DataFrame(data)
data_df.describe()

# %%
data_df['idade'].mean()

#%%
data_df['nome'].iloc[-1]