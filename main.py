from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! This is done via SSH tunnel -test"

@app.route("/hi")
def test():
    return "hi!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)