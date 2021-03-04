from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

def index():
    return "Welcome to the index page!"

@app.route("/hello/")
def hello():
    return "Hello there"

@app.route("/hello/<user>")
def hello(user):
    return f"Hello there, {user}!"