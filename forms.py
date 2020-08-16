"""Forms for Job Tracker"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
# Need to lookup image uplaod field
from wtforms.validators import DataRequired, Email, Length


class UserAddForm(FlaskForm):
    """Form for signing up a new user."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=7)])
    # Need to find wtforms image field
    # image_file = ('(Optional) Image File')


class UserEditForm(FlaskForm):
    """Form for editing existing user."""


class LoginForm(FlaskForm):
    """Login form"""
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[Length(min=7)])


class JobAddForm(FlaskForm):
    """Form for adding a new job."""
    company = StringField('Company name', validators=[DataRequired()])
    url = StringField('Company URL', validators=[DataRequired()])


class JobEditForm(FlaskForm):
    """Form for chaning job details."""
