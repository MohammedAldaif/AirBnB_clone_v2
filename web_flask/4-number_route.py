#!/usr/bin/python3
"""
this module prints HBNB when /hbnb page is requested
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/python/<text>/")
def python_text(text):
    """
    prints python followed by text string
    """
    text = text.replace("_", " ")
    if text:
        return f'Python {escape(text)}'
    else:
        return "Python is cool"


@app.route("/number/<int:n>")
def route_number(n):
    """
    prints n is a number , only if its an integer
    """
    return f'{escape(n)} is a number'


@app.route("/c/<text>")
def c_text(text):
    """
    prints c followed by text string
    """
    text = text.replace("_", " ")
    return f'C {escape(text)}'


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """
    this function print HBNB when /hbnb page is requested
    Return: string
    """
    return "HBNB"


@app.route("/", strict_slashes=False)
def hello_world():
    """
    this functuon prints Hello HBNB! when / page is requested
    Return: string
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
