import datetime

from flask import render_template, url_for, flash, redirect, request, abort
from expendoapp import app, db, bcrypt
from expendoapp.forms import LoginForm, RegistrationForm, AddExpense
from expendoapp.models import User, Expenses
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data,
					password=hashed_pw)
		db.session.add(user)
		db.session.commit()
		flash(f'Account successfully created for {form.email.data}!', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash("Login unsuccessful, please check your Login information.", "error")
	return render_template('login.html', title='Login', form=form)


#
# @app.route('/expense/new', methods=['GET', 'POST'])
# @login_required
# def addExpense():
# 	form = AddExpense()
# 	if form.validate_on_submit():
# 		expense = Expenses.query.filter_by(user_id=current_user.id).first()
# 		expense.rent += form.rent.data
# 		expense.groceries += form.groceries.data
# 		expense.bills += form.bills.data
# 		expense.transportation += form.transportation.data
# 		expense.entertainment += form.entertainment.data
# 		expense.vacation += form.vacation.data
# 		expense.miscellaneous += form.miscellaneous.data
# 		db.session.add(expense)
# 		db.session.commit()
# 		flash("Expenses successfully logged!", "success")
# 		return redirect(url_for('home'))
# 	return render_template('add_expense.html', form=form, title='Add Expenses')


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
	return render_template('account.html', title='Account')  #


@app.route('/expenses')
@login_required
def myExpenses():
	expense = Expenses.query.filter_by(user_id=current_user.id).first()
	return render_template('my_expenses.html', expense=expense, title='My Expenses')


@app.route('/expense/new', methods=['GET', 'POST'])
@login_required
def addExpense():
	form = AddExpense()
	if form.validate_on_submit():
		expense = Expenses.query.filter_by(user_id=current_user.id, date=datetime.date.today().strftime("%m-%y")).first()
		if expense:
			expense.rent += form.rent.data
			expense.groceries += form.groceries.data
			expense.bills += form.bills.data
			expense.transportation += form.transportation.data
			expense.entertainment += form.entertainment.data
			expense.vacation += form.vacation.data
			expense.miscellaneous += form.miscellaneous.data
		else:
			expense = Expenses(rent=form.rent.data, groceries=form.groceries.data, bills=form.bills.data,
							   transportation=form.transportation.data, entertainment=form.entertainment.data,
							   vacation=form.vacation.data, miscellaneous=form.miscellaneous.data,
							   date=datetime.date.today().strftime("%m-%y"), user_id=current_user.id)
		db.session.add(expense)
		db.session.commit()
		flash("Expenses successfully logged!", "success")
		return redirect(url_for('home'))
	return render_template('add_expense.html', form=form, title='Add Expenses')
#
#
