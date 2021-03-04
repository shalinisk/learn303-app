from flask import Flask
import os


app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the index page!"
    #return render_template('index.html')

@app.route("/hello/")
def hello():
    print("I am the hello function")
    return "Hello there"

@app.route("/hello/user/")
def hellouser():
    user = os.environ['USER']
    print("I am the hello user function")
    return f"Hello there, {user}!"

@app.route("/vars/")
def vars():
    for item, value in os.environ.items():
        print('{}: {}'.format(item, value))