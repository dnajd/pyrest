import boto
import dynamodb_mapper
from dynamodb_mapper.model import DynamoDBModel
from dynamodb_mapper.model import ConnectionBorg
from ddbmock import config
from ddbmock import connect_boto_patch
from db_models import TestMap

# mock
config.STORAGE_ENGINE_NAME = 'sqlite'                   # switch to sqlite backend
config.STORAGE_SQLITE_FILE = '/tmp/pyrest.sqlite'       # define the database path. defaults to 'dynamo.db'
db = connect_boto_patch()                               # Wire-up boto and ddbmock together

# connect
conn = ConnectionBorg()

# create table
conn.create_table(TestMap, 10, 10, False)
