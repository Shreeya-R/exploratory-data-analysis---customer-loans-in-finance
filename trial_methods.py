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