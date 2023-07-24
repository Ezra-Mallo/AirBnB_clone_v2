#!/usr/bin/python3
"""
A python script that starts a Flask web application
"""

from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def number_n_(n):
    """
    Returns a string indicating whether the provided input is a number.
    """
    return "{} is a number".format(str(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_n(n):
    """
    Return template only if n is an integer
    """
    return render_template("5-number.html", value=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
