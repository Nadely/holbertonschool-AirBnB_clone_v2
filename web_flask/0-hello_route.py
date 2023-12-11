#!/usr/bin/python3
<<<<<<< HEAD
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello HBNB!</p>"
=======
"""create route"""
from flask import Flask


app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'
>>>>>>> 2d72836 (starts a flask web application)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
