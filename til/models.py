from mongoengine import *
from til import login_manager
from flask_login import UserMixin
import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()
  

class User(Document, UserMixin):
    username = StringField(required=True, max_length=50)
    password = StringField(required=True, max_length=100)
    meta = {'collection': 'users'}

    def __repr__(self):
        return f"User('{self.username}')"


class Til(Document):
    SOURCE_REDDIT = 'reddit'
    SOURCE_TWITTER = 'twitter'
    SOURCE_YOUTUBE = 'youtube'
    SOURCES = (
        (SOURCE_REDDIT, 'Reddit'),
        (SOURCE_TWITTER, 'Twitter'),
        (SOURCE_YOUTUBE, 'Youtube')
    )
    code = StringField(required=True, unique=True)
    source = StringField(required=True, choices=SOURCES)
    author = StringField(required=True)
    content = StringField(required=True)
    extended = StringField()
    url = StringField()
    created = DateTimeField(default=datetime.datetime.utcnow)
    meta = {'collection': 'tils'}

    def __repr__(self):
        return f"Til('{self.code}', {self.content[:20]} '{self.created}')"
