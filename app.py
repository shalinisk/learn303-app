from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the index page!"
    #return render_template('index.html')

@app.route("/hello/")
def hello():
    return "Hello there"

@app.route("/hello/<user>")
def hello(user):
    return f"Hello there, {user}!"