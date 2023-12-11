#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State, City

app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    storage.close()

@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    states = storage.all(State)
    cities = None

    if id:
        key = "State." + id
        states = {key: storage.all(State).get(key)}
        cities = storage.all(City)

    return render_template('9-states.html', states=states, cities=cities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
