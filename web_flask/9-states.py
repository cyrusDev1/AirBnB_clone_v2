#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    states = storage.all(State)
    return render_template('9-states.html', states=states, id=None)


@app.route('/states/<id>', strict_slashes=False)
def state(id):
    states = storage.all(State)
    dico = {}
    for state in states.values():
        dico[state.id] = state
    state = dico.get(id)
    return render_template('9-states.html', states=states, state=state)


@app.teardown_appcontext
def close(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
