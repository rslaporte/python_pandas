# %%
import pandas as pd
# %%

#Statistics without using pandas
age = [30, 42, 90, 34]
mean_age = sum(age) / len(age)
print(mean_age)

variance_age = 0
for i in age:
    variance_age += (i - mean_age)**2

variance_age = variance_age / (len(age) - 1)
print(variance_age)

std_age = variance_age**(1/2)
print(std_age)


# %%
#Statistics using Pandas
series_age = pd.Series(age)

print(series_age.mean())
print(series_age.var())
print(series_age.std())
print(series_age.median())

# %%
series_age.describe()

# %%
#Navigation and indexes
series_age.index = ['A', 'B', 'C', 'D']

#Walk on series (geting by position)
print(series_age.iloc[0:2])

#Get element by index
print(series_age['A'])
print(series_age.loc['A'])