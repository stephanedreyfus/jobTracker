import os

from flask import Flask
from flas_debugtoolbar import DebugToolbasExtension
from models import db, connect_db, User, Job

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
