PyRest
======

Example building rest services in python and interacting with DynamoDB 

Setup
=====

Install pip, flask, boto, dynamodb-mapper

    sudo apt-get install pip
    pip install Flask
    pip install boto
    pip install dynamodb-mapper    
    pip install ddbmock
    

Documentation
==============

REST Python Package
* http://flask.pocoo.org/docs/quickstart/
* built on WSGI wrapper: http://werkzeug.pocoo.org/

DynamoDB Python Package
* https://pypi.python.org/pypi/dynamodb-mapper
* built on AWS wrapper: https://github.com/boto/boto
* mocking dynamodb: https://pypi.python.org/pypi/ddbmock/1.0.1
** helpful article on how to [setup mocks](http://stackoverflow.com/questions/14617160/how-to-use-ddbmock-with-dynamodb-mapper)
