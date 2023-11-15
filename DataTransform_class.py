# %%
import pandas as pd
loan_data = pd.read_csv('loan_payment.csv')
loan_data.head()
# %%
class DataTransform:
    '''
    This class converts the columns in the data to the correct format.
    '''

    def __init__(self, ):
        '''
        See help(DataTransform) for accurate signature.
        '''

    def object_to_datetime():
        '''
        This function converts object data types to datetime64 data types.

        Returns:

        '''
        loan_data['issue_date','earliest_credit_line','last_payment_date','next_payment_date', 'last_credit_pull_date'] = loan_data['issue_date','earliest_credit_line','last_payment_date','next_payment_date', 'last_credit_pull_date'].apply(pd.to_datetime)
        
    def object_to_boolean():
        '''
        This function converts object data types to boolean data types.

        Returns:

        '''
        loan_data['issue_date','earliest_credit_line','last_payment_date','next_payment_date', 'last_credit_pull_date'] = loan_data['issue_date','earliest_credit_line','last_payment_date','next_payment_date', 'last_credit_pull_date'].astype('bool')

    def object_to_category():
        '''
        This function converts object data types to category data types.

        Returns:

        '''
loan_data['issue_date','earliest_credit_line','last_payment_date','next_payment_date', 'last_credit_pull_date'] = loan_data['issue_date','earliest_credit_line','last_payment_date','next_payment_date', 'last_credit_pull_date'].astype('category')

    def object_to_timedelta():
        '''
        This function converts object data types to timedelta64 data types.

        Returns:

        '''
        loan_data['issue_date','earliest_credit_line','last_payment_date','next_payment_date', 'last_credit_pull_date'] = loan_data['issue_date','earliest_credit_line','last_payment_date','next_payment_date', 'last_credit_pull_date'].apply(pd.to_timedelta)