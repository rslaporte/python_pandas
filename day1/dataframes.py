# %%
import pandas as pd

# %%
data = {
    "name": ['Name1', 'Name2', 'Name3', 'Name4'],
    "lastname": ['Last1', 'Last2', 'Last3', 'Last4'],
    "idade": [30, 75, 23, 19],
    "peso": [33.75, 59.20, 104.28, 73.20]
}

# %%
#Creating a DataFrame
df = pd.DataFrame(data)
df

# %%
#Each column is a pd.Serie() element
df['idade']

# %%
#Type of each column
df.dtypes

# %%
#Describe method still works on Data Frames
describe = df.describe()
describe

describe['peso']['mean']

# %%
#Navigation methods
df.tail(2)
df.head(2)