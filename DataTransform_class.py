# %%
import pandas as pd
loan_data = pd.read_csv('loan_payment.csv')
loan_data.head()
# %%
class DataTransform:
    '''
    This class converts the columns in the data to the correct format.
    '''

    def __init__(self, data):
        '''
        See help(DataTransform) for accurate signature.
        '''
        self.data = data

    def object_to_datetime(self):
        '''
        This function converts object data types to datetime64 data types.

        Returns:

        '''
        self.data['issue_date'] = pd.to_datetime(self.data['issue_date'])
        self.data['earliest_credit_line'] = pd.to_datetime(self.data['earliest_credit_line'])
        self.data['last_payment_date'] = pd.to_datetime(self.data['last_payment_date'])
        self.data['next_payment_date'] = pd.to_datetime(self.data['next_payment_date'])
        self.data['last_credit_pull_date'] = pd.to_datetime(self.data['last_credit_pull_date'])
        
    def object_to_boolean(self):
        '''
        This function converts object data types to boolean data types.

        Returns:

        '''
        self.data['payment_plan', 'policy_code'] = self.data['payment_plan', 'policy_code'].astype('bool')

    def object_to_category(self):
        '''
        This function converts object data types to category data types.

        Returns:

        '''
        self.data['home_ownership', 'verification_status', 'loan_status'] = self.data['home_ownership', 'verification_status', 'loan_status'].astype('category')

    def object_to_timedelta(self):
        '''
        This function converts object data types to timedelta64 data types.

        Returns:

        '''
        self.data['issue_date','earliest_credit_line','last_payment_date','next_payment_date', 'last_credit_pull_date'] = self.data['issue_date','earliest_credit_line','last_payment_date','next_payment_date', 'last_credit_pull_date'].apply(pd.to_timedelta)

# %%
new_data = DataTransform(loan_data)
# %%
new_data.object_to_datetime()
# %%
new_data.data.dtypes
# %%
