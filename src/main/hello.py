from flask import Flask
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/fail')
def login():
    abort(401)

if __name__ == '__main__':
    app.run()
