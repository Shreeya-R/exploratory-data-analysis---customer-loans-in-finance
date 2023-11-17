# %%
import pandas as pd
from matplotlib import pyplot 
from statsmodels.graphics.gofplots import qqplot
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
        '''
        This function creates a histogram to check the normality of a variable.

        Returns:
            histogram: a single histogram plot of the variable required.
        '''
        hist_column = input("Please enter the variable here: ")
        self.data.hist(column = hist_column)

    def qqplot_to_check_normality(self):
        '''
        This function creates a Q-Q plot to check if teh variable follows a normal distribution.

        Returns:
            Q-Q plot:
        '''
        qqplot_column = input("Please enter the variable here: ")
        qq_plot = qqplot(self.data[qqplot_column], line = '45')
        pyplot.show()
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

    def mean_for_missing_values(self):
        '''
        This function imputes the mean in place of missing values.

        Use this function when the variable is numeric and the histogram is not skewed.

        Returns:

        '''
        variable_name = input("Please enter the variable whose missing values need to be imputed using the mean here: ")
        self.data[variable_name] = self.data[variable_name].fillna(self.data[variable_name].mean())

    def median_for_missing_values(self):
        '''
        This function imputes the median in place of missing values.

        Use this function when the data is numeric and the histogram is skewed.

        Returns:

        '''
        variable_name = input("Please enter the variable whose missing values need to be imputed using the mean here: ")
        self.data[variable_name] = self.data[variable_name].fillna(self.data[variable_name].median())
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
plots = Plotter()
# %%
# Check if data is skewed before imputing values using histogram
plots.hist_to_check_normality()
# %%
# Use q-q plot to identify the whether or not to impute mean, median or mode.
plots.qqplot_to_check_normality()
# %%
DataFrameTransform_data.median_for_missing_values()
# %%
DataFrameTransform_data.mean_for_missing_values()