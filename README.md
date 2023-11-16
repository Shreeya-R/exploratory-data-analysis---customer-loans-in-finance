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

## UNFINISHED CODE
- doc strings for RDSDatabaseConnector class in db_utils.py

