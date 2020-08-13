""""MongoDB models for Job Tracker"""

from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_mongoengine import MongoEngine

bcrypt = Bcrypt()
db = MongoEngine()


def connect_db(app):
    db.app = app
    db.init_app(app)
