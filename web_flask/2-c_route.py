#!/usr/bin/python3

"""
    Script that starts a Flask web app on 0.0.0.0:5000
    This script can access:
    1. the default url("/")
    2. the hbnb welcome page("/")
    3. the c page with custom text("/c/<text>")
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """ Returns a welcome message to 0.0.0.0:5000"""

    return "Hello HBNB!"


@app.route("/hbnb")
def hello_hbnb():
    ''' Returns HBNB'''

    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """ Displays C followed by value in 'text' variable"""

    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
