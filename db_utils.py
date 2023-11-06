# %%
class RDSDatabaseConnector:
    '''
    This class extracts data from the RDS database.

    Attributes;

    '''

    def __init__(self, credentials):
        '''
        See help(RDSDatabaseConnector) for accurate signature
        '''
        self.credentials = credentials
    
    def load_credentials(self, yaml_file):
        '''
        This function is used to load the credentials.yaml file.

        Args:
            yaml_file (yaml): a yaml file to be loaded through this function.

        Returns:
            dict: the dictionary representation of the credentials.
        '''
        import yaml

        with open(yaml_file, 'r') as f:
            credentials = yaml.safe_load(f)
        return credentials
    
    def initialise_SQLAlchemy(self):
        '''
        This function initialises a SQLAlchemy engine from the 'credentials'.

        Returns:

        '''
        from sqlalchemy import create_engine
        import pandas as pd

        engine = create_engine((f"{'postgresql'}+{'psycopg2'}://{credentials['RDS_USER']}:{credentials['RDS_PASSWORD']}@{credentials['RDS_HOST']}:{credentials['RDS_PORT']}/{credentials['RDS_DATABASE']}"))
        engine.execution_options(isolation_level='AUTOCOMMIT').connect()
    
    def data_to_Pandas_df(self):
        '''
        This function extracts data from the RDS database and returns it as a Pandas DataFrame.

        Returns:

        '''
        loan_payment = pd.read_sql_table('loan_payments', engine)
        return loan_payment.head(10)
# %%
# Trial loading yaml file
import yaml
# had a few issues installing yaml locally but sorted now
# python3.11 -m pip install pyyaml

with open('credentials.yaml', 'r') as f:
    credentials = yaml.safe_load(f)
credentials
# It worked!
# %%
credentials['RDS_DATABASE']
# %%
# Trial sqlalchemy engine
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine(f"{'postgresql'}+{'psycopg2'}://{credentials['RDS_USER']}:{credentials['RDS_PASSWORD']}@{credentials['RDS_HOST']}:{credentials['RDS_PORT']}/{credentials['RDS_DATABASE']}")
# %%