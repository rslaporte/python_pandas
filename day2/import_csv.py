# %%
import pandas as pd

# %%
df_customers = pd.read_csv('../data/customers.csv', sep=';')
df_customers

# %%
#DataFrame shape
df_customers.shape

# %%
#Memory usage
df_customers.info(memory_usage='deep')

# %%
#Describe
df_customers['Points'].describe()

# %%
# Getting the max value
condition = df_customers['Points'] == df_customers['Points'].max()
df_customers['Points'][condition]

# %%
# Getting the name which has the max points
df_customers[condition]['Name'].iloc[0]

# %%
# More filters
condition = (df_customers['Points'] > 1000) & (df_customers['Points'] < 2000)
df_customers[condition]

# %%
# Remember to copy when you want to manipulate a slice
df_customers_1000_2000 = df_customers[condition].copy()
df_customers_1000_2000['Points'] = df_customers_1000_2000['Points'] + 1000
df_customers_1000_2000

# %%
# Select multiple columns
df_customers[['UUID', 'Name']]

# %%
# Alphabetical order of column names:
alphabetical_columns = df_customers.columns.tolist()
alphabetical_columns.sort()
df_customer = df_customers[alphabetical_columns]


# %%
# Renaming columns
df_customer = df_customer.rename(columns = {"Name": "Nome",
                    "Points": "Pontos"})
df_customer

# %%
# Another method
df_customer.rename(columns = {"UUID" : "Id"}, inplace = True)
df_customer