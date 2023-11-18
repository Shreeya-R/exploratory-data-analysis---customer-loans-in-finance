# %%
import pandas as pd
from matplotlib import pyplot 
from statsmodels.graphics.gofplots import qqplot
# %%
import numpy as np
import seaborn as sns
# %%
from scipy import stats
from scipy.stats import yeojohnson
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
class Plotter:
    '''
    This class visualises insights from the data.
    '''

    def __init__(self, data):
        '''
        See help(Plotter) for accurate signature.
        '''
        self.data = data

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
        qq_plot = qqplot(self.data[qqplot_column], line = 'q')
        pyplot.show()
    
    def visualise_missing_values(self):
        '''
        This function creates a matrix in order to help visualise any null values in the DataFrame.

        Returns:
            matrix: white lines represent a null value, so if there are no null values then the matrix should have no white horizontal lines.
        '''
        import missingno as msno

        msno.matrix(self.data)

    def log_visualise(self):
        '''
        This function carries out the log function in order to help remove skewness and displays the output as a histogram.

        Returns:
            histogram: a histogram of the distribution of the data after the log transformation has been applied.
            skewness: the skewness value of the data after the log transformation is applied.
        '''
        skewed_variable = input('Please enter variable to be normalised here: ')
        log_variable = self.data[skewed_variable].map(lambda i: np.log(i) if i > 0 else 0)
        t = sns.histplot(log_variable, label = "Skewness: %.2f"%(log_variable.skew()))
        t.legend()
    
    def box_cox_visualise(self):
        '''
        This function carries out the Box-Cox transformation in order to help remove skewness and displays the output as a histogram.

        Returns:
            histogram: a histogram of the distribution of the data after the Box-Cox transformation has been applied.
            skewness: the skewness value of the data after the Box-Cox transformation is applied.
        '''
        skewed_variable = input('Please enter variable to be normalised here: ')
        boxcox_variable = self.data[skewed_variable]
        boxcox_variable = stats.boxcox(boxcox_variable)
        boxcox_variable = pd.Series(boxcox_variable[0])
        t = sns.histplot(boxcox_variable, label = "Skewness: %.2f"%(boxcox_variable.skew()))
        t.legend()

    def yeojohnson_visualise(self):
        '''
        This function carries out the Yeo-Johnson transformation in order to help remove skewness and displays the output as a histogram.

        Returns:
            histogram: a histogram of the distribution of the data after the Yeo-Johnson transformation has been applied.
            skewness: the skewness value of the data after the Yeo-Johnson transformation is applied.
        '''
        skewed_variable = input('Please enter variable to be normalised here: ')
        yeojohnson_variable = self.data[skewed_variable]
        yeojohnson_variable = stats.yeojohnson(yeojohnson_variable)
        yeojohnson_variable = pd.Series(yeojohnson_variable[0])
        t = sns.histplot(yeojohnson_variable, label = "Skewness: %.2f"%(yeojohnson_variable.skew()))
        t.legend()

# %%
class DataFrameTransform:
    '''
    This class performs EDA transformations on the data.
    '''

    def __init__(self, data):
        '''
        See help(DataFrameTransform) for accurate signature.
        '''
        self.data = data

    def drop_single_value_columns(self):
        '''
        This function drops all the columns containing only a single value in them.

        Returns:

        '''
        self.data.drop(columns = ['policy_code', 'application_type'], inplace = True)
        return self.data
    
    def drop_too_many_null(self):
        '''
        This function drops the variables that have over 50% null values.

        Returns:

        '''
        self.data.drop(columns = ['mths_since_last_record', 'mths_since_last_major_derog', 'mths_since_last_delinq', 'next_payment_date'], inplace = True)
        return self.data

    def drop_too_many_zeros(self):
        '''
        This function drops the variables that have 50,000+ values out of the the 54230 available values.

        Returns:

        '''
        self.data.drop(columns = ['total_rec_late_fee', 'recoveries', 'collection_recovery_fee', 'collections_12_mths_ex_med'], inplace = True)
        return self.data

    def drop_all(self):
        '''
        This function encompasses all the drop methods in this class into one.

        Returns:

        '''
        DataFrameTransform_data.drop_single_value_columns()
        DataFrameTransform_data.drop_too_many_null()    
        DataFrameTransform_data.drop_too_many_zeros()
        return self.data
    
    def drop_missing_value_rows(self):
        '''
        This function allows you to drop rows with missing values in them.

        Returns:

        '''
        column_to_drop_rows = input("Please enter the column you would like to drop NA values from here: ")
        self.data.dropna(subset = [column_to_drop_rows], inplace = True)
        return self.data

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

    def log_transformation(self):
        '''
        This function carries out the log function in order to help remove skewness and displays the output as a histogram.

        Returns:
            histogram: a histogram of the distribution of the data after the log transformation has been applied.
            skewness: the skewness value of the data after the log transformation is applied.
        '''
        skewed_variable = input('Please enter variable to be normalised here: ')
        log_variable = self.data[skewed_variable].map(lambda i: np.log(i) if i > 0 else 0)
        t = sns.histplot(log_variable, label = "Skewness: %.2f"%(log_variable.skew()))
        t.legend()
    
    def box_cox_transformation(self):
        '''
        This function carries out the Box-Cox transformation in order to help remove skewness and displays the output as a histogram.

        Returns:
            histogram: a histogram of the distribution of the data after the Box-Cox transformation has been applied.
            skewness: the skewness value of the data after the Box-Cox transformation is applied.
        '''
        skewed_variable = input('Please enter variable to be normalised here: ')
        boxcox_variable = self.data[skewed_variable]
        boxcox_variable = stats.boxcox(boxcox_variable)
        boxcox_variable = pd.Series(boxcox_variable[0], inplace = True)
        t = sns.histplot(boxcox_variable, label = "Skewness: %.2f"%(boxcox_variable.skew()))
        t.legend()

    def yeojohnson_transformation(self):
        '''
        This function carries out the Yeo-Johnson transformation in order to help remove skewness and displays the output as a histogram.

        Returns:
            histogram: a histogram of the distribution of the data after the Yeo-Johnson transformation has been applied.
            skewness: the skewness value of the data after the Yeo-Johnson transformation is applied.
        '''
        skewed_variable = input('Please enter variable to be normalised here: ')
        yeojohnson_variable = self.data[skewed_variable]
        yeojohnson_variable = stats.yeojohnson(yeojohnson_variable)
        yeojohnson_variable = pd.Series(yeojohnson_variable[0])
        t = sns.histplot(yeojohnson_variable, label = "Skewness: %.2f"%(yeojohnson_variable.skew()))
        t.legend()

# %%
# Look at percentange of NULL values
DataFrameInfo_data.percentage_of_NULL_values()
DataFrameInfo_data.mean_single_column()
DataFrameInfo_data.median_single_column()
# %%
# Create DataFrameTransform instance
DataFrameTransform_data = DataFrameTransform()
# %%
DataFrameTransform_data.drop_all()
DataFrameTransform_data.median_for_missing_values()
DataFrameTransform_data.mean_for_missing_values()
DataFrameTransform_data.drop_missing_value_rows()
# %%
# Create Plotter instance
plots = Plotter()
# %%
# Check if data is skewed before imputing values using histogram
plots.hist_to_check_normality()
# %%
# Use q-q plot to identify the whether or not to impute mean, median or mode.
plots.qqplot_to_check_normality()
# %%
plots.visualise_missing_values()
# %%
cleaned_data = DataFrameTransform_data.data

# Create a new csv file for the missing value cleaned data
cleaned_data.to_csv('cleaned_data', index = False)
# %%
# Read the newly created csv file
cleaned_data_final = pd.read_csv('cleaned_data.csv')
cleaned_data_final.info()
# %%
print(cleaned_data_final.select_dtypes('int64').skew())
print(cleaned_data_final.select_dtypes('float64').skew())

# Skewness threshold is acceptable between -2 and +2
# id                   2.370227
# member_id            2.205248
# delinq_2yrs          5.376385
# inq_last_6mths       3.253523
# annual_inc             8.717500
# out_prncp              2.354051
# out_prncp_inv          2.354471
# total_rec_int          2.204585
# last_payment_amount    2.497220
# %%
data_to_be_normalised = DataFrameTransform(cleaned_data_final)
# %%
data_to_be_normalised.log_transformation()
# %%
# Log Transformation effect
# delinq_2yrs -> 5.415423 (higher)
# inq_last_6mths -> 1.971073 (lower)
# annual_inc -> 0.139203 (perfect!) BEST
# out_prncp -> 0.574792 (nearly perfect!) BEST
# out_prncp_inv -> 0.574866 (nearly perfect!) BEST
# total_rec_int -> -0.562533 (slight left skew but perfect!)
# last_payment_amount -> 0.128038 (nearly perfect!)
# %%
data_to_be_normalised.box_cox_transformation()
# %%
# Box-Cox Transformation effect
# annual_inc -> -0.01 (perfect!)
# total_rec_int -> 0.00 (perfect!)
# rest of variables did not work due tot the values not being strictly +ve
# %%
data_to_be_normalised.yeojohnson_transformation()
# %%
# Yeo-Johnson Transformation effect
# delinq_2yrs -> 1.87 (lower) BEST
# inq_last_6mths -> 0.25 (lower) BEST
# out_prncp -> 0.53 (lower) BEST but not that different from log
# out_prncp_inv -> 0.53 (lower) BEST but same as above
# last_payment_amount -> 0.00 BEST