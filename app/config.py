import os

# user = os.environ['POSTGRES_USER']
# password = os.environ['POSTGRES_PASSWORD']
# host = os.environ['POSTGRES_HOST']
# database = os.environ['POSTGRES_DB']
# port = os.environ['POSTGRES_PORT']

user = 'user1'
password = 'password1'
host = '0.0.0.0'
database = 'contact'
port = 5432


DATABASE_CONNECTION_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'
