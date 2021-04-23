#!/usr/local/bin/python3

from flask import Flask

import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World !"

@app.route("/owner")
def owner():
    return f"Hello World from Raj Birru !!"

@app.route("/datetime")
def get_time():
    return f'{datetime.datetime.now()}'


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)
