# %%
import pandas as pd

# %%
df = pd.read_parquet("../data/transactions_cart.parquet")
df.info(memory_usage="deep")