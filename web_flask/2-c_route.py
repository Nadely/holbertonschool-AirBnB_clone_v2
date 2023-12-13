#!/usr/bin/python3
"""Write a script that starts a Flask web application"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Return Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """return HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """return C + text"""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == '__main__':
    """main"""
    app.run(host='0.0.0.0', port=5000)
