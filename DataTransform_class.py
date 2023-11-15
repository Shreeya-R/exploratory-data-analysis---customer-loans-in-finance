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
            datatype (datetime): specified columns are now datetime datatypes.
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
            datatype (boolean): specified columns are now boolean datatypes.
        '''
        self.data['payment_plan'] = self.data['payment_plan'].astype('bool')

    def object_to_category(self):
        '''
        This function converts object data types to category data types.

        Returns:
            datatype (category): specified columns are now category datatypes.
        '''
        self.data['home_ownership'] = self.data['home_ownership'].astype('category')
        self.data['verification_status'] = self.data['verification_status'].astype('category')
        self.data['loan_status'] = self.data['loan_status'].astype('category')
        self.data['purpose'] = self.data['purpose'].astype('category')
        
    def object_to_integer(self):
        '''
        This function converts object data types to integer data types.

        Returns:
            datatype (int): specified columns are now integer datatypes.
        '''
        self.data['term'] = self.data['term'].apply(lambda x: 36 if x == '36 months' else 60)
        
        #self.data['employment_length'] = self.data['employment_length'].apply(lambda x: 5 if x == '5 years')

# %%
new_data = DataTransform(loan_data)
# %%
new_data.object_to_datetime()
# %%
new_data.object_to_boolean()

# %%
new_data.object_to_category()
# %%
new_data.object_to_integer()
# %%
new_data.data.dtypes
# %%
new_data.data['employment_length']
# %%
