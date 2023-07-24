#!/usr/bin/python3
"""
A python script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Display a greeting message
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_():
    """
    Display a message
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space)
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text=None):
    """
    Display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space)
    """
    if text is not None:
        return "Python {}".format(text.replace("_", " "))
    return "Python is cool"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
