"""Forms for Job Tracker"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
# Need to lookup image uplaod field
from wtforms.validators import DataRequired, Email, Length


class UserAddForm(FlaskForm):


class UserEditForm(FlaskForm):


class LoginForm(FlaskForm):


class JobAddForm(FlaskForm):


class JobEditForm(FlaskForm):
