# %%
# Load loan_payment.csv into a Pandas DataFrame
import pandas as pd

loan_data = pd.read_csv('loan_payment.csv')
# %%
# Load first 10 rows of data
loan_data.head(10)
# %%
# Find shape of data
loan_data.shape

# Tells us that in the data there are:
# 54,231 rows
# 43 columns
# %%
# Describe data
loan_data.describe
loan_data.info
loan_data.sample

# All of the above appear to give more or less the same information.
# %%

# %%
