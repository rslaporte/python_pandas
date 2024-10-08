#  %%
import pandas as pd

# %%
data_01 = {
    "id": [1,2,3,4],
    "name": ["A", "B", "C", "D"],
    "age": [30,40,20,25]
}

df_01 = pd.DataFrame(data_01)

data_02 = {
    "id": [5,6,7,8],
    "name": ["E", "F", "G", "H"],
    "age": [14,15,25,73]
}

df_02 = pd.DataFrame(data_02)

# %%
pd.concat([df_01, df_02]).reset_index(drop=True)


# %%
data_03 = {
    "last_name": ["X", "Y", "Z", "W"],
    "value": [3000, 4250, 3230, 2555],
}

df_03 = pd.DataFrame(data_03)

pd.concat([df_01, df_03], axis=1).reset_index(drop=True)