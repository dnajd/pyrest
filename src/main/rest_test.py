import boto
import dynamodb_mapper
from dynamodb_mapper.model import DynamoDBModel
from dynamodb_mapper.model import ConnectionBorg
from ddbmock import config
from ddbmock import connect_boto_patch

###########################
# Dynamo DB Model
class TestMap(DynamoDBModel):
    __table__ = u"test_map"
    __hash_key__ = u"test_key"
    __schema__ = {
        u"test_key": int,
        u"name": unicode,
    }