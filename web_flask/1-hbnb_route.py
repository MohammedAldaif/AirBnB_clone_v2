#!/usr/bin/python3
"""
this module prints HBNB when /hbnb page is requested
"""
from flask import Flask

app = Flask(__name__)


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
