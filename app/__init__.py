from flask import Flask
from dotenv import load_dotenv
import os
# from flask_login import LoginManager

from .models import create_db, Article, Image, Tag, Topic, User, drop_db


load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACKMODIFICATION'] = os.getenv('STM')

# # Створення менеджера логінів і підключення його до програми.
# login_manager = LoginManager()
# login_manager.init_app(app)

