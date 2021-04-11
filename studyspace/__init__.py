from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
#interacts with app.py to run the app
#secret key that prevents things like cookies from being modified
#randomly generated key by hand
app.config['SECRET_KEY'] = '2314gea02d1a4e9ca461e3ca54290a9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#initializes the app to work with the given imports
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'success'
from studyspace import routes


