from flask import Flask
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_pyfile('settings.py')

db = MongoEngine()
db.init_app(app)

bcrypt = Bcrypt()
login_manager = LoginManager(app)

from til import terminal
from til import views
