#!/usr/bin/python3
""" this module prints a simple string using flask """
from flask import Flask

app = Flask(__name__)

@app.route("/",strict_slashes=False)
def hello_world():
    """
    This function returns a simple greeting message.

    Returns:
        str: A string saying "Hello HBNB!".
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
