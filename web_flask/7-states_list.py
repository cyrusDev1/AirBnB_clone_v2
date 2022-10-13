#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
