import boto
from ddbmock import config
from ddbmock import connect_boto_patch

# switch to sqlite backend
config.STORAGE_ENGINE_NAME = 'sqlite'
# define the database path. defaults to 'dynamo.db'
config.STORAGE_SQLITE_FILE = '/tmp/pyrest.sqlite'

# Wire-up boto and ddbmock together
db = connect_boto_patch()
