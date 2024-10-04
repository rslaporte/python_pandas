# %%
import pandas as pd

# %%
df = pd.read_csv('../data/products.csv', 
                       sep=';',
                       # head=None, se tiver o atributo names
                       names=['Id', 'Name', 'Description'] )
df

# %%
df.rename(columns={"Name": "Nome",
                     "Description": "Descrição"},
                     inplace=True)
df