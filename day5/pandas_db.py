# %%
import pandas as pd
import sqlalchemy

# %%
engine = sqlalchemy.create_engine("sqlite:///../data/database.db")


# %%
df_customers = pd.read_sql_table("customers", engine)

# %%
query = '''
SELECT * FROM customers AS t1
LEFT JOIN transactions AS t2
ON t1.UUID = t2.IdCustomer
LIMIT 10'''

df_customers2 = pd.read_sql_query(query, engine)
df_customers2

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
df_01.to_sql("tb_pandas_db", engine, index=False, if_exists="replace")