from flask import Flask
import flask_migrate
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a5861ca271e02884a96bc6076e9b82ed'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://kktgsycvkeircs:c696cc5e9dc12633a67ca529268d300908a9ef05222260af764a5ddf0b710cc1@ec2-34-193-44-192.compute-1.amazonaws.com:5432/dkm8bdpto8lm7"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


from expendoapp import routes



# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:15957535@localhost/expendo"
