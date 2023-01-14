#!/usr/bin/python3

"""Displaying data in a list"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_db():
    """Close connection to the storage"""

    storage.close()


@app.route("/states_list")
def states_list():
    """Renders an HTML page"""

    states = storage.all('State').values()
    states = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
