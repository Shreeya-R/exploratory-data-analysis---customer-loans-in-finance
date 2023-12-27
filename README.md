# EDA on Customer Loans in Finance
Very short description here.

## Contents
1. The Project
2. Installation Instructions
3. Usage Instructions
4. File Structure of the Project
5. License Information

## 1. The Project
### Description 
- Aim & purpose of this project
- A rough outline of the class RDSDatabaseConnector

### What I've Learned
1. How to filter columns with missing values
- Median as missing value: when variable is numerical & skewed
- Mean as missing value: when variable is numerical & not skewed
- Mode as missing value: when variable is numerical or categorical?
2. Practically applying the knowledge
- funded_amount: impute the median for missing values due to histogram & qqplot indicating skewness to the right.
- int_rate: impute the median for missing values due to histogram & qqplot indicating skewness to the right.
- employment_length: impute the median/mode due to skewness & the distribution not being close to that of a normal one
- last_payment_date: remove missing value rows due to it not being normally distributed & percentage of missing data being very low (0.1346%)
- last_credit_pull_date: remove missing value rows due to it not being close to a normal distribution & percentage of missing data being extremely low (0.0129%)

## 2. Installation Instructions
- import yaml
- import pandas etc if not included in code of the class
- import db_utils.py 

## 3. Usage Instructions
Go through class RDSDatabaseConnector & go through each method.
- load_credentials (loads the credentials.yaml file to give the dictionary for credentials)
- initialise_SQLAlchemy (initialises the SQLAlchemy engine)

## 4. File Structure of the Project
- db_utils.py 
    - This connects to the RDS
    - Converts data to pandas dataframe
    - Converts pandas dataframe to csv
- familiarise_with_data.py
    - Loads loan_payment 
    - Looks at familiarises self with data
- DataTransform_class.py
    - Converts columns to correct data format
    - Contains the class DataTransform, and corresponding methods
- DataFrameInfo.py
    - Extracts information from the DataFrame and it's columns
    - Contains methods to generate useful information about the DataFrame
- missing_values.py
    - Deals with missing data values
    - Creates 2 classes to deal with missing values
    - impute mean when data is numeric & not skewed
    - impute median when data is numeric & skewed
    - impute mode when data i sstring(object) or numeric

## UNFINISHED CODE
- doc strings for RDSDatabaseConnector class in db_utils.py
- Clean up misisng values file using a .ipynb file
- Update details in this file 

# Project Outline
1. [Extracting Data from the Cloud](https://github.com/shhrreeyyaa/exploratory-data-analysis---customer-loans-in-finance?tab=readme-ov-file#1-extracting-data-from-the-cloud)
2. [Exploratory Data Analysis (EDA)](https://github.com/shhrreeyyaa/exploratory-data-analysis---customer-loans-in-finance?tab=readme-ov-file#2-exploratory-data-analysis-eda)
3. [Analysis and Visualisation](https://github.com/shhrreeyyaa/exploratory-data-analysis---customer-loans-in-finance?tab=readme-ov-file#3-analysis-and-visualisation)

## 1. Extracting Data from the Cloud
In order to begin the data analysis, I first needed to extract and clean the data. To do this, I created a class called __RDSDatabaseConnector__ in a new file, db_utils.py, which has the sole purpose of extracting the data. Other than pandas, all other necessary packages for this class are already coded to be imported within the method that they are required.

To create an instance for this class and use it's methods, one needs to first create a yaml file, which contains the credentials of the RDS database that you want to connect to. Make sure that the credentials contain the following information:

- RDS_HOST
- RDS_PASSWORD
- RDS_USER
- RDS_DATABASE
- RDS_PORT

There are a total of 5 different methods contained in the __RDSDatabaseConnector__ class:

1. init
2. load_credentials
3. initialise_SQLAlchemy
4. data_to_Pandas_df
5. df_to_csv

Below is a brief outline on each method. Further information on the RDSDatabaseConnector class can be found using help(RDSDatabaseConnector) after the class has been imported to your computer.

### 1. init
This magic method simply initialises the instance attributes with the values that have be passed as arguments. In the RDSDatabaseConnector class, there is only one attribute initialised in this method, which is 'self.credentials'. 

### 2. load_credentials
The purpose of this method is to load the credentials yaml file so that this information can later be used to connect to the RDS. I had to create a credentials yaml file with the necessary information and import the yaml Python package prior to this step.

### 3. initialise_SQLAlchemy
Now that the the credentials had been loaded in Python, the next step was to use the information to connect to the SQLAlchemy engine and load the data. In order to create an SQLAlchemy, the engine package first needed to be imported from sqlalchemy.

### 4. data_to_Pandas_df
Finally, the required data had been extracted. However the format of the data at this point was not ideal for data analysis, hence a method was created to convert this data to a pandas dataframe. This resulted in the data being encompassed in a variable name called 'pandas_df'.

### 5. df_to_csv
Unfortunately, a pandas dataframe can only be viewed in Python and so is not easily accessible after each coding session. To solve this inconvenience, I converted the data to a csv, which means that the data can be saved locally on my computer and can also be accessible to any peers that I wish to share the raw data with. 

## 2. Exploratory Data Analysis (EDA)


## 3. Analysis and Visualisation

