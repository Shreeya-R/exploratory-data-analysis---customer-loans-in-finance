# %%
class RDSDatabaseConnector:
    '''
    This class extracts data from the RDS database.

    Attributes;

    '''

    def __init__(self, ):
        '''
        See help(RDSDatabaseConnector) for accurate signature
        '''
    
    def load_credentials(self):
        '''
        This function is used to load the credentials.yaml file.

        Returns:

        '''
        import yaml
        with open('credentials.yaml', 'r') as f:
            credentials = yaml.safe_load(f)
        print(credentials)

# %%
# Trial loading yaml file
import yaml
# had a few issues installing yaml locally but sorted now
# python3.11 -m pip install pyyaml

with open('credentials.yaml', 'r') as f:
    credentials = yaml.safe_load(f)
print(credentials)
# It worked!
# %%
