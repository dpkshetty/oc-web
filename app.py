from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World Again'

@app.route('/test')
def process_test():
    return 'Hello! You are accessing /test endpoint'

@app.route('/version')
def get_version():
    return 'App version (using generic webhook): <b>1.0</b>'
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
