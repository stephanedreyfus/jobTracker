"""MongoDB models for Job Tracker"""

from flask_mongoengine import (
    MongoEngine,
    Document,
    StringField,
    EmailField,
    ImageField,
    DateTimeField,
    EmbeddedDocumentField,
    ListField,
    UrlField,
)

from flask_bcrypt import Bcrypt
from datetime import datetime

bcrypt = Bcrypt()
db = MongoEngine()


class Job(Document):
    company = StringField(max_length=120, required=True)
    url = UrlField(required=True)
    applied = DateTimeField(default=datetime.utcnow, required=True)
    tech_interview = DateTimeField()
    onsite = DateTimeField()
    rejected = DateTimeField()


class User(Document):
    # Need id field
    name = StringField(max_length=120, required=True, unique=True)
    email = EmailField(allow_utf8_user=True, required=True)
    password = StringField(max_length=50, min_length=7, required=True)
    jobs = ListField(EmbeddedDocumentField(Job))
    image = ImageField(
        size=(300, 300, True),
        thumbnail_size=(150, 150),
        default="/static/images/profile.png",
    )
    created_on = DateTimeField(default=datetime.utcnow)

    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {len(self.jobs)}"

    # Not requiring jobs yet, and not including in signup. Hopefully
    # will still be able to add later.
    @classmethod
    def signup(cls, username, email, password, image):
        """ Sign up user.

        Hashes password and adds user to system."""

        hashed_pwd = bcrypt.generate_password_hash.decode("UTF-8")

        user = User(
            username=username,
            email=email,
            password=hashed_pwd,
            image=image,
        )

        user.save()
        return user


def connect_db(app):
    """Call this in app.py to connect to db"""

    db.app = app
    db.init_app(app)
