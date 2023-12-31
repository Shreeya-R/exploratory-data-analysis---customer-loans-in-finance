# %%
import pandas as pd
import numpy as np
# %%
loan_data = pd.read_csv('loan_payment.csv')
loan_data.head()
# %%
from Classes.DataTransform_class import DataTransform
# %%
# Transform data using the DataTransform clss
DataTranform_data = DataTransform(loan_data)
DataTranform_data.all_transformations()
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

    def mean_of_variable(self):
        '''
        This function calculates the mean of a single column.

        Returns:
            mean (string): a string description of the mean for the chosen single column.
            data (column): all the data contained in the chosen single column.
        '''
        single_column = input("Please enter the column you wish to calculate the mean of here: ")
        single_column_mean = self.data[single_column].mean()

        print(f"Mean of {single_column} is: {single_column_mean}\n")
        print(f"Data for {single_column} is: \n{self.data[single_column]}")

    def median_of_variable(self):
        '''
        This function calculates the median of a single column.

        Returns:
            median (string): a string description of the median for the chosen single column.
            data (column): all the data contained in the chosen single column.
        '''
        single_column = input("Please enter the column you wish to calculate the median of here: ")
        single_column_median = self.data[single_column].median()

        print(f"Median of {single_column} is: {single_column_median}\n")
        print(f"Data for {single_column} is: \n{self.data[single_column]}")
    
    def mode_of_variable(self):
        '''
        This function calculates the mode of a single column.

        Returns:
            mode (string): a string description of the mode for the chosen single column.
            data (column): all the data contained in the chosen single column.
        '''
        single_column = input("Please enter the column you wish to calculate the mode of here: ")
        single_column_mode = self.data[single_column].mode()

        print(f"Mode of {single_column} is: {single_column_mode}\n")
        print(f"Data for {single_column} is: \n{self.data[single_column]}")

    def std_dev_of_variable(self):
        '''
        This function calculates the standard deviation of a single column.

        Returns:
            standard deviation (string): a string description of the standard deviation for the chosen single column.
            data (column): all the data contained in the chosen single column.
        '''
        single_column = input("Please enter the column you wish to calculate the standard deviation of here: ")
        single_column_std_dev = self.data[single_column].std()

        print(f"Standard deviation of {single_column} is: {single_column_std_dev}\n")
        print(f"Data for {single_column} is: \n{self.data[single_column]}")

    def skew_of_variable(self):
        '''
        This function calculates the skew of a single column.

        Returns:
            skew (string): a string description of the skew for the chosen single column.
            data (column): all the data contained in the chosen single column.
        '''
        single_column = input("Please enter the column you wish to calculate the skew of here: ")
        single_column_skew = self.data[single_column].skew()

        print(f"Skew of {single_column} is: {single_column_skew}\n")
        
        if single_column_skew > 1:
            print('This indicates a strong positive (right) skew.')
        elif single_column_skew < -1:
            print('This indicates a strong negative (left) skew.')
        else:
            print('This indicates that the data is normal or close to normal in distribution.')

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
    #DataFrameInfo_data.mode_single_column()
# %%
if __name__ == "__main__": 
    cleaned_missing_value_data = pd.read_csv('cleaned_data.csv')

    cleaned_data = DataFrameInfo(cleaned_missing_value_data)
    cleaned_data.std_dev_of_variable()
    cleaned_data.skew_of_variable()
# %%
