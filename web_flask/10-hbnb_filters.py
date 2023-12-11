#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State, City, Amenity


app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    storage.close()

@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters(id=None):
    states = storage.all(State)
    cities = None

    if id:
        key = "State." + id
        states = {key: storage.all(State).get(key)}
        cities = storage.all(City)
        amenities = storage.all(Amenity)

    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
