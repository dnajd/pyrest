import boto
import dynamodb_mapper
from dynamodb_mapper.model import DynamoDBModel
from dynamodb_mapper.model import ConnectionBorg
from ddbmock import config
from ddbmock import connect_boto_patch
from flask import Flask
from db_models import TestMap

###########################
# ddbmock

config.STORAGE_ENGINE_NAME = 'sqlite'                   # switch to sqlite backend
config.STORAGE_SQLITE_FILE = '/tmp/pyrest.sqlite'       # define the database path. defaults to 'dynamo.db'
db = connect_boto_patch()                               # Wire-up boto and ddbmock together

###########################
# Flash routes

# create app
app = Flask(__name__)

# POST: /test/new
@app.route('/test/new', methods=['GET'])
def post_test():
    t1 = TestMap()
    t1.test_key = 1
    t1.name = u"Hello World"
    t1.save()
    return "success"


# GET: /test/int:id
@app.route('/test/<int:id>', methods=['GET'])
def get_test(id):
    t1 = TestMap.get(id)
    return t1.name

# connect and run
if __name__ == '__main__':

    # Dynamo DB Connection
    conn = ConnectionBorg()

    # run app
    app.run(debug=True)