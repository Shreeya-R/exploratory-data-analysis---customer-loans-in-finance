# %%
class RDSDatabaseConnector:
    '''
    This class extracts data from the RDS database.

    Attributes;

    '''

    def __init__(self, dictionary_credentials):
        '''
        See help(RDSDatabaseConnector) for accurate signature
        '''
        self.dictionary_credentials = dictionary_credentials
    
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
            dictionary_credentials = yaml.safe_load(f)
        return dictionary_credentials
    
    def initialise_SQLAlchemy(self):
        '''
        This function initialises a SQLAlchemy engine from the 'dictionary_credentials'.
        '''

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
