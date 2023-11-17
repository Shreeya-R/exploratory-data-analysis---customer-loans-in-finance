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
# Look at sample of size 30 of the data
loan_data.sample(30)
# %%
# Describe data
loan_data.info()

# All of the above appear to give more or less the same information.
# %%
# Check data types of the data
loan_data.dtypes

# Change:
# term from object -> timedelta64
# grade from object -> string
# subgrade from object -> string
# employment_length from object -> timedelta64
# home_ownership from object -> category 
# verification_status from object -> category 
# issue_date from object -> datetime64
# loan_staus from object -> category (cut down some categories)
# payment_plan from object -> boolean (yes & no values)
# %%
# Check home_ownership values are categorical
print(loan_data['home_ownership'].nunique())
print(loan_data['home_ownership'].unique())

# has 5 unique values
# unique values are 'MORTGAGE', 'RENT', 'OWN', 'OTHER', 'NONE'
# %%
# Check verification_status values are categorical
print(loan_data['verification_status'].nunique())
print(loan_data['verification_status'].unique())

# has 3 unique values
# unique values are 'Not Verified' 'Source Verified' 'Verified'
# %%
# Check loan_status values are categorical
print(loan_data['loan_status'].nunique())
print(loan_data['loan_status'].unique())

# has 9 unique values
# unique values are 'Current' 'Fully Paid' 'Charged Off' 'Late (31-120 days)' 'In Grace Period' 'Late (16-30 days)' 'Default' 'Does not meet the credit policy. Status:Fully Paid' 'Does not meet the credit policy. Status:Charged Off'
# %%
print(loan_data['payment_plan'].nunique())
print(loan_data['payment_plan'].unique())

# this is a boolean variable
# %%
print(loan_data['purpose'].nunique())
print(loan_data['purpose'].unique())

# has 14 unique values
# unique values are 'credit_card' 'debt_consolidation' 'home_improvement' 'small_business' 'renewable_energy' 'major_purchase' 'other' 'moving' 'car' 'medical' 'house' 'vacation' 'wedding' 'educational'
# %%
print(loan_data['earliest_credit_line'])

# %%
print(loan_data['application_type'].nunique())
print(loan_data['application_type'].unique())

# only has 1 value, so doesn't add any information for us
# %%
print(loan_data['term'].nunique())
print(loan_data['term'].unique())
# %%
print(loan_data['policy_code'].nunique())
print(loan_data['policy_code'].unique())

# only has 1 value, so doesn't add any information for us
# %%
print(loan_data['employment_length'].nunique())
print(loan_data['employment_length'].unique())
print(loan_data['employment_length'].dtype)
# %%
print(loan_data['total_rec_late_fee'].astype('int64'))
print(loan_data['total_rec_late_fee'].value_counts()[0])
# %%
print(loan_data['recoveries'].astype('int64'))
print(loan_data['recoveries'].value_counts()[0])
# %%
print(loan_data['collection_recovery_fee'].astype('int64'))
print(loan_data['collection_recovery_fee'].value_counts()[0])
# %%
print(loan_data['collections_12_mths_ex_med'].isna().sum())
print(loan_data['collections_12_mths_ex_med'].astype('int64', errors='ignore'))
print(loan_data['collections_12_mths_ex_med'].value_counts()[0])
# %%
print(loan_data['employment_length'].unique())
print(loan_data['employment_length'].nunique())
print(loan_data['employment_length'].isnull().sum())
# %%
