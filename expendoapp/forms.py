from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from expendoapp.models import User
from datetime import datetime

class RegistrationForm(FlaskForm):
	first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
	last_name = StringField('Last Name ', validators=[DataRequired(), Length(min=2, max=20)])
	email = EmailField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=30)])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That Email is already registered!')


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')


class AddExpense(FlaskForm):
	rent = IntegerField('Rent', default=0)
	groceries = IntegerField('Groceries', default=0)
	bills = IntegerField('Bills', default=0)
	transportation = IntegerField('Transportation', default=0)
	entertainment = IntegerField('Entertainment', default=0)
	vacation = IntegerField('Vacation', default=0)
	miscellaneous = IntegerField('Miscellaneous', default=0)
	submit = SubmitField("Submit Expenses", default=0)
#

