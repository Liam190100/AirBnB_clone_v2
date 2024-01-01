#!/usr/bin/python3
"""
Runs a Flask web application
"""

from ../models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """ Displays HTML page of all States sorted by name """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """ This get out the current SQLAlchemy session. """
    storage.close()


if __name__ == "__main__":
    """ Run on 0.0.0.0 """
    app.run(host='0.0.0.0')
