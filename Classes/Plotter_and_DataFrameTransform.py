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
            histogram: a histogram plot of the chosen variable.
        '''
        hist_column = input("Please enter the variable here: ")
        self.data.hist(column = hist_column)

    def qqplot_to_check_normality(self):
        '''
        This function creates a Q-Q plot to check if the variable follows a normal distribution.

        Returns:
            Q-Q plot: a quartile-quartile plot for the chosen variable.
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
    
    def boxplot_for_outliers(self):
        '''
        This function creates a boxplot, which can then be used to identify the presence of outliers in the data.

        Returns:
            boxplot: a boxplot for a specific variable.
        '''
        plt.figure(figsize = (30,5))
        self.data.boxplot()
        plt.show()

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
            cleaned data: data with the necessary columns removed.
        '''
        self.data.drop(columns = ['policy_code', 'application_type', 'payment_plan'], inplace = True)
        return self.data
    
    def drop_too_many_null(self):
        '''
        This function drops the variables that have over 50% null values.

        Returns:
            cleaned data: data with the necessray columns removed.
        '''
        self.data.drop(columns = ['mths_since_last_record', 'mths_since_last_major_derog', 'mths_since_last_delinq', 'next_payment_date'], inplace = True)
        return self.data

    def drop_too_many_zeros(self):
        '''
        This function drops the variables that have 50,000+ values out of the the 54230 available values.

        Returns:
            cleaned data: data with the necessary columns removed.
        '''
        self.data.drop(columns = ['total_rec_late_fee', 'recoveries', 'collection_recovery_fee', 'collections_12_mths_ex_med'], inplace = True)
        return self.data

    def drop_all(self):
        '''
        This function encompasses all the drop methods in this class into one.

        Returns:
            cleaned data: data with the necessary columns removed.
        '''
        self.drop_single_value_columns()
        self.drop_too_many_null()    
        self.drop_too_many_zeros()
        return self.data
    
    def drop_missing_value_rows(self):
        '''
        This function allows you to drop rows with missing values in them.

        Returns:
            cleaned data: data with the missing value rows removed.
        '''
        column_to_drop_rows = input("Please enter the column you would like to drop NA values from here: ")
        self.data.dropna(subset = [column_to_drop_rows], inplace = True)
        return self.data

    def mean_for_missing_values(self):
        '''
        This function imputes the mean in place of missing values.

        Use this function when the variable is numeric and the histogram is not skewed.

        Returns:
            total null values: should be zero now that the column has been filled with the mean.
        '''
        variable_name = input("Please enter the variable whose missing values need to be imputed using the mean here: ")
        self.data[variable_name] = self.data[variable_name].fillna(self.data[variable_name].mean())
        return self.data[variable_name].isnull().sum()

    def median_for_missing_values(self):
        '''
        This function imputes the median in place of missing values.

        Use this function when the data is numeric and the histogram is skewed.

        Returns:
            total null values: should be zero now that the column has been filled with the median.
        '''
        variable_name = input("Please enter the variable whose missing values need to be imputed using the mean here: ")
        self.data[variable_name] = self.data[variable_name].fillna(self.data[variable_name].median())
        return self.data[variable_name].isnull().sum()
    
    def log_transformation(self):
        '''
        This function carries out the log function to the entire column in order to remove skewness from the variable.

        Returns:
            transformed column (log): the column of the new transfomed variable.
        '''
        skewed_variable = input('Please enter variable to be normalised here: ')
        self.data[skewed_variable] = self.data[skewed_variable].map(lambda i: np.log(i) if i > 0 else 0)
        return self.data[skewed_variable]
    
    def box_cox_transformation(self):
        '''
        This function carries out the Box-Cox transformation to the entire column in order to remove skewness from the variable.

        Returns:
            transformed column (box-cox): the column of the new transfomed variable.
        '''
        skewed_variable = input('Please enter variable to be normalised here: ')
        boxcox_variable = self.data[skewed_variable]
        boxcox_variable = stats.boxcox(boxcox_variable)
        boxcox_variable = pd.Series(boxcox_variable[0])

        self.data[skewed_variable] = boxcox_variable
        return self.data[skewed_variable]

    def yeojohnson_transformation(self):
        '''
        This function carries out the Yeo-Johnson transformation to the entire column in order to remove skewness from the variable.

        Returns:
            transformed column (yeo-johnson): the column of the new transfomed variable.
        '''
        skewed_variable = input('Please enter variable to be normalised here: ')

        yeojohnson_variable = self.data[skewed_variable]
        yeojohnson_variable = stats.yeojohnson(yeojohnson_variable)
        yeojohnson_variable = pd.Series(yeojohnson_variable[0])

        self.data[skewed_variable] = yeojohnson_variable
        return self.data[skewed_variable]
    
    def IQR_for_outliers(self):
        '''
        This function useds the inner quartile range (IQR) to decide the boundaries that outliers lie within and removes them from the specified variable.

        Returns:
            outliers (string): the outliers for the variable.
        '''
        variable = input("Please enter the variable you wish to remove outliers from here: ")

        # Calculate lower and upper quartiles
        Q1 = self.data[variable].quantile(0.25)
        Q3 = self.data[variable]. quantile(0.75)

        print(f"Q1 (25th Percentile): {Q1}")
        print(f"Q3 (75th Percentile): {Q3}")

        # Caluclate the IQR
        IQR = Q3 - Q1

        print(f"IQR (Inner Quartile Range): {IQR}")

        # Identify outliers
        lower_outliers = self.data[(self.data[variable] < (Q1 - 1.5*IQR))]
        upper_outliers = self.data[(self.data[variable] > (Q3 + 1.5*IQR))]

        print(f"Outliers:\n{lower_outliers[variable]}\n{upper_outliers[variable]}")
        print(f"Unique values of the outliers:\n{lower_outliers[variable].unique()}\n{upper_outliers[variable].unique()}")
        
    def remove_outliers_IQR(self):
        '''
        This function removes the rows with outliers using the inner quartile range.

        Returns:
            data: the column of the variable whose outliers have been removed. 
        '''
        variable = input("Please enter the variable you wish to remove outliers from here: ")

        Q1 = self.data[variable].quantile(0.25)
        Q3 = self.data[variable]. quantile(0.75)

        IQR = Q3 - Q1
        lower = Q1 - 1.5*IQR
        upper = Q3 + 1.5*IQR

        upper_array = np.where(self.data[variable] > upper)[0]
        lower_array = np.where(self.data[variable] < lower)[0]

        # Remove outliers
        self.data.drop(index = upper_array, inplace = True)
        self.data.drop(index = lower_array, inplace = True)

        return self.data 