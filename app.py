from flask import Flask
from flas_debugtoolbar import DebugToolbasExtension
from models import db, connect_db, User, Job

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///jobtrack"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
