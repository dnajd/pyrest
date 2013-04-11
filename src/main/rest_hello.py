from flask import Flask

# create app
app = Flask(__name__)

# GET: /hello
@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello World!'

# GET: /fail
@app.route('/fail', methods=['GET'])
def login():
    abort(401)

# run app
if __name__ == '__main__':
    app.run()