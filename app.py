from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the index page!"
    #return render_template('index.html')

@app.route("/hello/")
def hello():
    print("I am the hello function")
    return "Hello there"

@app.route("/hello/<user>")
def hello(user):
    print("I am the hello user function")
    return f"Hello there, {user}!"