#!/usr/bin/python3
"""Script that starts a flask web application
Setting the web application to listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays "Hello HBNB!" for route: /"""
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hello():
    """displays "HBNB" for route: /hbnb"""
    return ('HBNB')


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """displays /c/<text>: display “C ” followed by the value of the text
    variable (replace underscore _ symbols with a space )"""
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python/', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """display Python followed by the value of the text variable"""
    return ('Python ' + text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display /number/<n>: display “n is a number” only if n is an integer"""

    if isinstance(n, int):
        return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ displays a HTML page only if n is an integer
    format:
        - "Number: n" inside body tag"""
    return render_template('5-number.html', value=n)



@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """displays a HTML page only if n is an integer
    format:
        - H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    return render_template('6-number_odd_or_even.html', value=n)


if __name__ == '__main__':
    """ main function"""
    app.run(host='0.0.0.0', port=5000)
