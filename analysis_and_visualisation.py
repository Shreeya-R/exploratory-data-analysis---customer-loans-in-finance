# %%
import pandas as pd
import seaborn as sns
# %%
# Load the EDA data
removed_outliers= pd.read_csv('removed_outliers_data.csv')
# %%
#############################################################################
# Current state of loans
# What % of loans are recovered against the investor funding & total amount funded?
# %%
# 1)
# Investor funding
print(f"The sum of all investor funding is: {removed_outliers['funded_amount_inv'].sum()}")

# Total payment of loan recovered to investors?
print(f"The sum of all payments received for investor funding: {removed_outliers['total_payment_inv'].sum()}")

# Percentage recovered
(removed_outliers['total_payment_inv'].sum())/(removed_outliers['funded_amount_inv'].sum())
# loans from investment funding are 91.1% recovered
# %%
# Visualise
sns.scatterplot(x = removed_outliers['funded_amount_inv'], y = removed_outliers['total_payment_inv'])
# %%
# 2)
# Total amount funded
print(f"The sum of all investor funding is: {removed_outliers['funded_amount'].sum()}")

# Total payment of loan for total amount funded?
print(f"The sum of all payments receuved for investor funding: {removed_outliers['total_payment'].sum()}")

# Percentage recovered
(removed_outliers['total_payment'].sum())/(removed_outliers['funded_amount'].sum())
# loans from total funded amount are 91.9% recovered
# %%
# Visualise
sns.scatterplot(x = removed_outliers['funded_amount'], y = removed_outliers['total_payment'])
# %%
# 3)
# Amount recovered up to 6 months in the future

# Filter out loans that are full paid
current = removed_outliers[removed_outliers['loan_status'].str.contains('Current')]

# Instalment sto be received in future 6 months
instalment = current['instalment']*6
print(f"Instalments to be received in next 6 months: {instalment}")

# Total instalments for next 6 months
sum_instalment = instalment.sum()
print(f"Total instalments for next 6 months: {sum_instalment}")

# Total recovered in 6 months
total_recovered_6mths = sum_instalment + (removed_outliers['total_payment'].sum())
print(f"Total recovered in 6 months: {total_recovered_6mths}")

# Percentage of total funded and total recovered
percentage_recovered_6mths = total_recovered_6mths/(removed_outliers['funded_amount'].sum())
print(f"Percentage recovered after 6 months: {percentage_recovered_6mths*100}")

# Percentage recovered is estimated to be 99.04% for the current loans.
# %%
# Visualise
sns.scatterplot(x = removed_outliers['funded_amount'], y = (instalment + (removed_outliers['total_payment'])))
# %%
#############################################################################
# Calculating loss
# Calculate the % of charged off loans historically and the amount paid before charged off.
# %%
# 1)
# Charged off loans
charged_off  = removed_outliers[removed_outliers['loan_status'].str.contains('Charged Off')]
print(f"The data with charged off loan status is:\n{charged_off['loan_status']}")

# Number of charged off loans
total_charged_off = charged_off['loan_status'].count()
print(f"The total loans charged off is: {total_charged_off}")

# Percentage of loans charged off
total_loans = removed_outliers['loan_status'].count()
percentage_charged_off = (total_charged_off/total_loans)*100
print(f"The percentage of loans historically charged off is: {percentage_charged_off}%")

# Percentage charged off is 10.84%
# %%
# 2)
# Amount paid before charged off

# Sum of payments made to loans
sum_payments_charged_off = charged_off['total_payment'].sum()
print(f"The amount paid before charged off is: {sum_payments_charged_off}")

# Loan amount for charged off loans
loan_amount_charged_off = charged_off['loan_amount'].sum()
print(f"The total of loans that were charged off: {loan_amount_charged_off}")

# Percentage of loans paid before charged off
percentage_paid_before_charged_off = (sum_payments_charged_off/loan_amount_charged_off)*100
print(f"The percentage of the loan paid before charged off is: {percentage_paid_before_charged_off}%")

# Percentage paid before charged off is 49.36%
# %%
#############################################################################
# Calculate projected loss