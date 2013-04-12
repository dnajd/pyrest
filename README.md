PyRest
======

Example building rest services in python and interacting with DynamoDB 

Setup
=====

Pip & sqlite

    sudo apt-get install pip    
    sudo apt-get install sqlite3 libsqlite3-dev

Pip Install Python Packages: pip, flask, boto, dynamodb-mapper, urllib, httplib, json


PyRest Scripts
==============
Run these scripts to see the example code work

1. Create a mock dynamo db

   python src/main/db_create.py

2. Start rests services (in separate terminal)

   python src/main/rest_test.py

3. Post data through rest service to mock dynamo db

   # arg1=int arg2=string
   python src/main/post_rest_test.py 1 'hello world'

4. Read back the data by browsing to REST service /test/1    

5. Clean up the mock dynamodb

   rm /tmp/pyrest.sqlite

Resources
==============

REST Python Package
* http://flask.pocoo.org/docs/quickstart/
* built on WSGI wrapper: http://werkzeug.pocoo.org/

DynamoDB Python Package
* https://pypi.python.org/pypi/dynamodb-mapper
* built on AWS wrapper: https://github.com/boto/boto
* mocking dynamodb: https://pypi.python.org/pypi/ddbmock/1.0.1
 * helpful article on how to [setup mocks](http://stackoverflow.com/questions/14617160/how-to-use-ddbmock-with-dynamodb-mapper)
