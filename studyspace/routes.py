from flask import render_template, url_for, flash, redirect, request
from studyspace import app, db, bcrypt
from studyspace.forms import RegistrationForm, LoginForm, SurveyForm
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
        return redirect(url_for('newSurvey'))
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


@app.route("/map", methods=['GET', 'POST'])
def map():
    return render_template('map.html', title='Map')


@app.route("/survey", methods=['GET', 'POST'])
def survey():
    form = SurveyForm()
    if form.validate_on_submit():
        User.groups = form.group
        User.study = form.course
        db.session.commit()
        return redirect(url_for('map'))
    else:
        flash('Invalid Class, try again.')
    return render_template('survey.html', title='Survey', form=form)

@app.route("/newSurvey", methods=['GET', 'POST'])
def newSurvey():
    form = SurveyForm()
    if form.validate_on_submit():
        User.major = request.form['major']
        User.groups = form.group
        User.study = form.course
        db.session.commit()
        return redirect(url_for('map'))
    else:
        flash('Invalid Class, try again.')
    return render_template('newSurvey.html', title='New Account Survey', form=form)


@app.route("/about")
def about():
    return render_template('about.html', title='about')


@app.route("/findGroup")
def findGroup():
    return render_template('findGroup.html', title='Find Group')


@app.route("/birdLibrary")
@login_required
def birdLibrary():
    return render_template('birdLibrary.html', title='Bird Library')


@app.route("/lifeScienceBuilding")
@login_required
def lifeScienceBuilding():
    return render_template('lifeScienceBuilding.html', title='Life Science Building')


@app.route("/link")
@login_required
def link():
    return render_template('link.html', title='Link')


@app.route("/falk")
@login_required
def falk():
    return render_template('falk.html', title='Falk')


@app.route("/newhouse")
@login_required
def newhouse():
    return render_template('newhouse.html', title='Newhouse')


@app.route("/whitman")
@login_required
def whitman():
    return render_template('whitman.html', title='Whitman')


@app.route("/confirmation")
@login_required
def confirmation():
    return render_template('confirmation.html', title='Confirm Room')