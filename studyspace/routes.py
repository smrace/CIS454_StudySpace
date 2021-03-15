from flask import render_template, url_for, flash, redirect, request
from studyspace import app, db, bcrypt
from studyspace.forms import RegistrationForm, LoginForm
from studyspace.database import User, Building, Group, Room, Amenities, Subject, Reservation, RoomAmenities, StudentSubject
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    return render_template('mainPage.html')


#Look at if statement for when redirecting after reserving room
@app.route("/createAccount", methods=['GET', 'POST'])
def createAccount():
    if current_user.is_authenticated:
        return redirect(url_for('survey'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, emailAddress=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account successfully created!', 'success')
        return redirect(url_for('login'))
    return render_template('createAccount.html', title='Create Account', form=form)


#see forms.py for more info on LoginForm() and RegistrationForm()
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('survey'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(emailAddress=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('survey'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


#takes user to profile that they are signed into
@app.route("/profile")
@login_required
def profile():
    return render_template('profile.html', title='Profile')


@app.route("/mainPage")
def mainPage():
    return render_template('mainPage.html', title='Main Page')


@app.route("/map")
def map():
    return render_template('map.html', title='Map')


@app.route("/survey")
def survey():
    return render_template('survey.html', title='Survey')


@app.route("/about")
def about():
    return render_template('about.html', title='about')


@app.route("/findGroup")
def findGroup():
    return render_template('findGroup.html', title='Find Group')