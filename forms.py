"""Forms for Job Tracker"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField, FileField
from wtforms.validators import DataRequired, Email, Length, Optional, Regexp


class UserAddForm(FlaskForm):
    """Form for signing up a new user."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=7)])
    image = FileField(
        'User Image',
        validators=[Optional(), Regexp('(?i)\.(jpg|png|gif|pdf)$')]
        )


class UserEditForm(FlaskForm):
    """Form for editing existing user."""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=7)])
    image = FileField(
        'User Image',
        validators=[Optional(), Regexp('(?i)\.(jpg|png|gif|pdf)$')]
        )


class LoginForm(FlaskForm):
    """Login form"""
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[Length(min=7)])


class JobAddForm(FlaskForm):
    """Form for adding a new job."""
    company = StringField('Company name', validators=[DataRequired()])
    url = StringField('Company URL', validators=[DataRequired()])


class JobEditForm(FlaskForm):
    """Form for changing job details.
       It should not be possible to change the applied/created date."""
    company = StringField('Company name', validators=[DataRequired()])
    url = StringField('Company URL', validators=[DataRequired()])
    tech_interview = DateTimeField(
        'Technical Interview Date',
        validators=[Optional()],
        )
    onsite = DateTimeField('Onsite Date', validators=[Optional()])
    rejected = DateTimeField('Rejection Date', validators=[Optional()])
