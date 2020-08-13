import os

from flask import Flask, render_template, session, g
from flas_debugtoolbar import DebugToolbasExtension
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_mongoengine import MongoEngine

bcrypt = Bcrypt()
db = MongoEngine()

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'jobtracker',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "blank tomatoes")
toolbar = DebugToolbasExtension(app)


#####################################################################
# Splash page/user login/signup


@app.before_request
def add_user_tog():
    """If user logged in, add curr user to Flask global"""

    if CURR_USER_KEY in session:
        g.user - User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    "Logout user."

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup."""
