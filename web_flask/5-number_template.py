#!/usr/bin/python3
"""
Script that runs an app with Flask framework:
Routes:
    * /: display “Hello HBNB!”
    * /hbnb: display “HBNB”
    * /c/<text>: display “C ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    * /python/(<text>): display “Python ”,and the value of the text variable
    (replace underscore _ symbols with a space )
        The default value of text is “is cool”
    * /number/<n>: display “n is a number” only if n is an integer
    * /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY

"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """/ route """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """/hbnb route """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """/c/<text> route """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """/python/<text> route """
    if text is not 'is cool':
        text = text.replace('_', ' ')
    return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """/number/<n> route """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """/number_template/<n> route """
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
