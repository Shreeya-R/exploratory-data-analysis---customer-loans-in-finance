# %%
import pandas as pd
import numpy as np
# %%
loan_data = pd.read_csv('loan_payment.csv')
loan_data.head()
# %%
from DataTransform_class import DataTransform
# %%
# Transform data using the DataTransform clss
DataTranform_data = DataTransform(loan_data)
DataTranform_data.all_transformations()
# %%
DataTranform_data.data.info()
# %%
class DataFrameInfo:
    '''
    This class extracts information from the DataFrame and it's columns.
    '''
    def __init__(self, data):
        '''
        See help(DataFrameInfo) for accurate signature.
        '''
        self.data = data

    def mean_single_column(self):
        '''
        This function calculates the mean of a single column.

        Returns:
            mean (string): a string description of the mean for the chosen single column.
            data (column): all the data contained in the chosen single column.
        '''
        single_column = input("Please enter the column you wish to calculate the mean of here: ")
        single_column_mean = self.data[single_column].mean()

        print(f"Mean of {single_column} is {single_column_mean}.\n")
        print(f"Data for {single_column} is: \n{self.data[single_column]}")

    def median_single_column(self):
        '''
        This function calculates the median of a single column.

        Returns:
            median (string): a string description of the median for the chosen single column.
            data (column): all the data contained in the chosen single column.
        '''
        single_column = input("Please enter the column you wish to calculate the median of here: ")
        single_column_median = self.data[single_column].median()

        print(f"Median of {single_column} is {single_column_median}.\n")
        print(f"Data for {single_column} is: \n{self.data[single_column]}")

    def extract_mean_all(self):
        '''
        This function calculates the mean of numerical columns.

        Returns:
            means (column): the mean of each numerical column
        '''
        int64_means = self.data.select_dtypes('int64').mean()
        float64_means = self.data.select_dtypes('float64').mean()

        print(f"Mean values of all numerical columns are:\n \n{int64_means}\n{float64_means}")

    def extract_standard_dev_all(self):
        '''
        This function calculates the standard deviation of the numerical columns.
        
        Returns:
            standard deviation: the standard deviation of each numerical column.
        '''
        int64_standard_dev = self.data.select_dtypes('int64').std()
        float64_standard_dev = self.data.select_dtypes('float64').std()
        
        print(f"Standard deviation values of all numerical columns are:\n \n{int64_standard_dev}\n{float64_standard_dev}")
    
    def extract_median_all(self):
        '''
        This function calculates the median of the numerical columns.

        Returns:
            median: the median of each numerical column.
        '''
        int64_median = self.data.select_dtypes('int64').median()
        float64_median = self.data.select_dtypes('float64').median()
        
        print(f"Median values of all numerical columns are:\n \n{int64_median}\n{float64_median}")

    def all_statistical_measures(self):
        '''
        This function calculates all the statistical measures.
        
        This is equivalent to using the .describe() on any DataFrame, but this function makes it easier to code.

        Returns:
            statistics (table): a statistical overview of all numerical columns.
        '''
        statistical_overview = self.data.describe()
        return statistical_overview
    
    def distinct_values(self):
        '''
        This function counts the distinct values of the categorical columns.

        Returns:
            distinct values: the number of distinct values for each category column.
        '''
        number_of_distinct_values = self.data.select_dtypes('category').nunique()
        print(f"The number of distinct values for each category column is: \n{number_of_distinct_values}")

    def shape_of_df(self):
        '''
        This functions finds the shape of the DataFrame.

        Returns:
            rows (string): a statement for the number of rows in the DataFrame.
            columns (string): a statement for the number of columns in the DataFrame.
        '''
        rows = self.data.shape[0]
        print(f"Rows: {rows}")

        columns = self.data.shape[1]
        print(f"Columns: {columns}")

    def percentage_of_NULL_values(self):
        '''
        This function calculates the percentage of NULL values in each column.

        Returns:
            percentage of null values (string): the percentage of null values in all columns.
        '''
        null_values = self.data.isnull().sum()/len(self.data) 
        print(f"The percentage of NULL values is: \n{null_values}")
# %%
if __name__ == "__main__":  
    DataFrameInfo_data = DataFrameInfo(DataTranform_data.data)
    
    #DataFrameInfo_data.extract_mean_all()
    #DataFrameInfo_data.extract_standard_dev_all()
    #DataFrameInfo_data.extract_median_all()
    #DataFrameInfo_data.all_statistical_measures()
    #DataFrameInfo_data.distinct_values()
    #DataFrameInfo_data.shape_of_df()
    #DataFrameInfo_data.percentage_of_NULL_values()
    #DataFrameInfo_data.mean_single_column()
    #DataFrameInfo_data.median_single_column()
# %%
