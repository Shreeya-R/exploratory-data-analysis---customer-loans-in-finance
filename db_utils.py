# %%
import pandas as pd

# %%
class RDSDatabaseConnector:
    '''
    This class extracts data from the RDS database.

    Attributes:

    '''

    def __init__(self, credentials):
        '''
        See help(RDSDatabaseConnector) for accurate signature
        '''
        self.credentials = credentials
    
    def load_credentials(self):
        '''
        This function is used to load the credentials.yaml file.

        Args:
            yaml_file (yaml): a yaml file to be loaded through this function.

        Returns:
            dict: the dictionary representation of the credentials.
        '''
        import yaml

        with open(self.credentials, 'r') as f:
            load_credentials = yaml.safe_load(f)

        self.credentials = load_credentials
    
    def initialise_SQLAlchemy(self):
        '''
        This function initialises a SQLAlchemy engine from the 'credentials'.

        Returns:

        '''
        from sqlalchemy import create_engine

        engine = create_engine((f"{'postgresql'}+{'psycopg2'}://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"))
        engine.execution_options(isolation_level='AUTOCOMMIT').connect()

        return engine
    
    def data_to_Pandas_df(self):
        '''
        This function extracts data from the RDS database and returns it as a Pandas DataFrame.

        Returns:

        '''
        pandas_df = pd.read_sql_table('loan_payments', engine)
        return pandas_df
    def df_to_csv(self):
        '''
        This function converts as Pandas DataFrame to a csv file, which is saved to your local machine.

        Returns:

        '''
        csv_file = pandas_df.to_csv('loan_payment', index=False)
        return csv_file
# %%
#if __name__ == 'main':
new_rds = RDSDatabaseConnector('credentials.yaml')
new_rds
# %%
new_rds.load_credentials()
# %%
new_rds.initialise_SQLAlchemy()
# %%
new_rds.data_to_Pandas_df()
# %%
new_rds.df_to_csv()
# %%
