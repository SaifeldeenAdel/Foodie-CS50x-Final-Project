from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager
from urllib.parse import quote_plus

app = Flask(__name__)
app.jinja_env.filters['quote_plus'] = lambda u: quote_plus(u)
app.config['SECRET_KEY'] = '1b6e6ff21daa8629c7b3ee11383a3d1b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from application import routes