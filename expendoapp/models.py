from expendoapp import db, login_manager
from expendoapp import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	first_name = db.Column(db.String(20), nullable=False)
	last_name = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	expenses = db.relationship('Expenses', backref='owner', lazy="dynamic")

	def __repr__(self):
		return f"User('{self.id}, {self.first_name}, {self.last_name}, {self.email}, {self.password}')"


# NEED TO MAKE CONNECTING TABLE FOR DATABASE

class Expenses(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	rent = db.Column(db.Integer())
	bills = db.Column(db.Integer())
	groceries = db.Column(db.Integer())
	transportation = db.Column(db.Integer())
	entertainment = db.Column(db.Integer())
	vacation = db.Column(db.Integer())
	miscellaneous = db.Column(db.Integer())
	date = db.Column(db.String, nullable=False, )
	user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)



	def __repr__(self):
		return f"Expense#('{self.id}, {self.user_id}')"