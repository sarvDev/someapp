from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def func():
    return render_template("home.html")

@app.route("/hello")
def hello():
    return "Hello, World"