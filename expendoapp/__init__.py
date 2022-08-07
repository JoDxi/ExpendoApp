from flask import Flask
# import os
import flask_migrate
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a5861ca271e02884a96bc6076e9b82ed'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:15957535@localhost/expendo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


from expendoapp import routes