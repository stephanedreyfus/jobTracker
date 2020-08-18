import os

from flask import Flask, render_template, session, g, redirect, flash
from flas_debugtoolbar import DebugToolbasExtension
from forms import (
    UserAddForm,
    UserEditForm,
    LoginForm,
    JobAddForm,
    JobEditForm,
    )
from models import connect_db, User
from flask_mongoengine import NotUniqueError
# from werkzeug.utils import secure_filename

# # Need to figure out where to send this for Mongoengine.
# UPLOAD_FOLDER = '/path/to/the/uploads'
# ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'gif'}
CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'jobtracker',
    'host': 'localhost',
    'port': 27017
}

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "blank tomatoes")
toolbar = DebugToolbasExtension(app)

connect_db(app)

#####################################################################
# Splash page/user login/signup


@app.before_request
def add_user_to_g():
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

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data,
                email=form.email.data,
                image=form.image.data,
            )

            user.save()

        except NotUniqueError as e:
            flash(f"{e}: Username already exists", 'danger')
            return render_template('users/signup.html', form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template('users/signup.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm

    if form.validate_on_submit():
        user = User.authenticate(
            form.username.data,
            form.password.data,
            )

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/")

        flash("Invalide credentials.", "danger")

    return render_template('users/login.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()

    flash("You have successfully logged out.", "success")
    return redirect("/login")


# ###################################################################
# General user routes
