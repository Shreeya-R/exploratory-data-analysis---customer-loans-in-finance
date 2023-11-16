# %%
import pandas as pd
import matplotlib.pyplot as plt 
# %%
# Load in data
loan_data = pd.read_csv('loan_payment.csv')
# %%
# Transform datatype of columns
from DataTransform_class import DataTransform
DataTransform_data = DataTransform(loan_data)
DataTransform_data.all_transformations()
# %%
# Import class for extracting data
from DataFrameInfo_class import DataFrameInfo
DataFrameInfo_data = DataFrameInfo(DataTransform_data.data)
# %%
# Look at percentange of NULL values
DataFrameInfo_data.percentage_of_NULL_values()
# %%
class Plotter:
    '''
    This class visualises insights from the data.
    '''

    def __init__(self):
        '''
        See help(Plotter) for accurate signature.
        '''
        self.data = DataFrameTransform_data.data

    def hist_to_check_normality(self):
        self.data['funded_amount'].hist(bins=40)
# %%
class DataFrameTransform:
    '''
    This class performs EDA transformations on the data.
    '''

    def __init__(self):
        '''
        See help(DataFrameTransform) for accurate signature.
        '''
        self.data = DataFrameInfo_data.data

    def drop_single_value_columns(self):
        '''
        This function drops all the columns containing only a single value in them.

        Returns:

        '''
        self.data.drop(columns = ['policy_code', 'application_type'], inplace = True)
    
    def drop_too_many_null(self):
        '''
        This function drops the variables that have over 50% null values.

        Returns:

        '''
        self.data.drop(columns = ['mths_since_last_record', 'mths_since_last_major_derog', 'mths_since_last_delinq', 'next_payment_date'], inplace = True)

    def drop_too_many_zeros(self):
        '''
        This function drops the variables that have 50,000+ 0 values out of the the 54230 available values.

        Returns:

        '''
        self.data.drop(columns = ['total_rec_late_fee', 'recoveries', 'collection_recovery_fee', 'collections_12_mths_ex_med'], inplace = True)

    def impute_missing_values(self):
        '''
        This function imputes missing values to the remaining columns.

        Returns:

        '''
        self.data['funded_amount'] = self.data['funded_amount'].fillna(self.data['funded_amount'].mean())
# %%
DataFrameTransform_data = DataFrameTransform()
# %%
DataFrameTransform_data.drop_single_value_columns()
# %%
DataFrameTransform_data.drop_too_many_null()
# %%
DataFrameTransform_data.drop_too_many_zeros()
# %%
DataFrameTransform_data.data
# %%
DataFrameInfo_data.all_statistical_measures()
# %%
DataFrameInfo_data.extract_median()
# %%
DataFrameTransform_data.impute_missing_values()
# %%
# Funded amount
# median = 12,000
# mean = 13,229
# %%
plots = Plotter()
# %%
plots.hist_to_check_normality()
# %%
