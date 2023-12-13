#!/usr/bin/python3
"""Write a script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Return State: <state.id>: <B><state.name></B>"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    """main"""
    app.run(host='0.0.0.0', port=5000)
