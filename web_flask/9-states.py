#!/usr/bin/python3
"""Write a script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """return cities if have state id"""
    states = storage.all(State).values()
    state = None

    if id is None:
        return render_template('9-states.html', states=states)

    for state in states:
        if id == state.id:
            return render_template('9-states.html', states=states)


if __name__ == '__main__':
    """main"""
    app.run(host='0.0.0.0', port=5000)
