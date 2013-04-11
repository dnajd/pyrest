import boto
import dynamodb_mapper
from dynamodb_mapper.model import DynamoDBModel
from dynamodb_mapper.model import ConnectionBorg
from ddbmock import config
from ddbmock import connect_boto_patch
from test_map import TestMap

###########################
# ddbmock
config.STORAGE_ENGINE_NAME = 'sqlite'                   # switch to sqlite backend
config.STORAGE_SQLITE_FILE = '/tmp/pyrest.sqlite'       # define the database path. defaults to 'dynamo.db'
db = connect_boto_patch()                               # Wire-up boto and ddbmock together

# Dynamo DB Connection
conn = ConnectionBorg()
conn.create_table(TestMap, 10, 10) #, wait_for_active=True) # create table
