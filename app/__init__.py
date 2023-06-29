from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
# from models import User

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login = LoginManager(app)
# @login.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)
login.login_view = 'login'
login.login_message_category = 'warning'


from app import routes, models
