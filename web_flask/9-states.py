from flask import Flask, render_template, abort
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    states = storage.all("State").values()
    states = sorted(states, key=lambda state: state.name)
    return render_template("states.html", states=states)


@app.route('/states/<string:state_id>', strict_slashes=False)
def state(state_id):
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    cities = sorted(state.cities, key=lambda city: city.name)
    return render_template("state.html", state=state, cities=cities)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
