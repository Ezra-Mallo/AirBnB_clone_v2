#!/usr/bin/python3
"""Script that starts a flask web application
Setting the web application to listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''
    displays "Hello HBNB!" for route: /
    '''
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hello():
    '''
    displays "HBNB" for route: /hbnb
    '''
    return ('HBNB')


if __name__ == '__main__':
    ''' main function '''
    app.run(host='0.0.0.0', port=5000)
