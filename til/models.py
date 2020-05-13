from mongoengine import *
from til import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()
  

class User(Document, UserMixin):
    username = StringField(required=True, max_length=50)
    password = StringField(required=True, max_length=100)
    meta = {'collection': 'users'}

    def __repr__(self):
        return f"User('{self.username}')"
