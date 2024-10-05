# %% 
import pandas as pd
import numpy as np

# %%
df = pd.read_csv("../data/customers.csv", sep=";")
df

# %%
#Generating new columns
df["Points_double"] = df["Points"] * 2
df

# %%
df["Points_ratio"] = df["Points_double"] / df["Points"]
df

# %%
df["Constant"] = 1
df

# %%
df["Points_log"] = np.log(df["Points"])
df

# %%
np.log(df[["Points", "Points_double", "Points_ratio"]])

# %%
#Uppercase - intuitive mode (bad)
upper_list = []
for i in df["Name"]:
    upper_list.append(i.upper())

df["Upper_names"] = upper_list
df
# %%
#Uppercase - Good Examples
df["Upper_names"] = df["Name"].str.upper()
df

# %%
def before_underscore(name):
    name = name.upper()
    return name.split("_")[0]

df["Before_underscore"] = df["Name"].apply(before_underscore)
df

# %%
#Lambda functions
before_underscore_lambda = lambda name: name.split("_")[0]

#So, the sugar is like:
df["Before_underscore"] = df["Name"].apply(lambda name: name.upper().split("_")[0])
df

# %%
# Last three characters from UUID
df["UUID"].apply(lambda x: x[-3:])

# %%
#Some 'filter' columns
def classification(points):
    if points < 1000 :
        return "low"
    elif points < 2000 :
        return "medium"
    return "high"

df["Classification"] = df["Points"].apply(classification)
df

# %%
data = {
    "name": ["A", "B", "C", "D"],
    "last_purchase": [1, 30, 10, 45],
    "value": [100, 2000, 15, 500],
    "frequency" : [2, 5, 1, 15]
}

df_crm = pd.DataFrame(data)

#You can apply a row to a function like this:
# df.apply(function, axis=1) ---This will pass each line of dataFrame as a parameter to function
