#!/usr/bin/python3

""" Script that starts a Flask web app on 0.0.0.0:5000 """

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """ Returns a welcome message to 0.0.0.0:5000"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    ''' Returns HBNB'''
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ Displays C followed by value in 'text' variable"""
    text = text.replace("_", " ")
    return f"C {text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
