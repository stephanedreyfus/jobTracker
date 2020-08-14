"""MongoDB models for Job Tracker"""

from flask_bcrypt import Bcrypt
from datetime import datetime

bcrypt = Bcrypt()
db = MongoEngine()

db.app = app
db.init_app(app)
