from flask import render_template, url_for, flash, redirect, request
from studyspace import app, db, bcrypt
from studyspace.forms import RegistrationForm, LoginForm, SurveyForm, BuildingForm
from studyspace.database import User, Building, Group, Room, Amenities, Subject, Reservation
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
        user = User(emailAddress=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account successfully created!', 'success')
        return redirect(url_for('newSurvey'))
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
    def validate_course():
        exists = False
        classes = ['MAT 101', 'ENG 101', 'SCI 101', 'GEO 101']
        for p in classes:
            if(form.course.data == p):
                exists = True
        if(exists != True):
            return False
        else:
            return True
    if form.validate_on_submit():
        
        if validate_course():
            #current_user.groupName.studyType = form.group.data
            current_user.study = form.course.data
            print(current_user.study)
            db.session.commit()
            print(current_user.study)
            return redirect(url_for('map'))
        else:
            flash(current_user.emailAddress)
            flash('Invalid Class, try again.' , 'danger')
    return render_template('survey.html', title='Survey', form=form)

@app.route("/newSurvey", methods=['GET', 'POST'])
def newSurvey():
    form = SurveyForm()
    def validate_course():
        exists = False
        classes = ['MAT 101', 'ENG 101', 'SCI 101', 'GEO 101']
        for p in classes:
            if(form.course.data == p):
                exists = True
        if(exists != True):
            return False
        else:
            return True
    if form.validate_on_submit():
        if validate_course():
            #current_user.groupName.studyType = form.group.data
            #current_user.major = form.request['major']
            current_user.study = form.course.data
            print(current_user.study)
            db.session.commit()
            print(current_user.study)
            return redirect(url_for('map'))
        else:
            flash(current_user.emailAddress)
            flash('Invalid Class, try again.' , 'danger')

    else:
        flash('Invalid Class, try again.')
    return render_template('newSurvey.html', title='New Account Survey', form=form)


@app.route("/about")
def about():
    return render_template('about.html', title='about')


@app.route("/findGroup")
@login_required
def findGroup():
    myUser = User.query.all()
    return render_template('findGroup.html', title='Find Group', myUser=myUser)


@app.route("/birdLibrary", methods=['GET', 'POST'])
@login_required
def birdLibrary():
    form = BuildingForm()
    rooms = Room.query.filter_by(building_id='2').all()
    amens = Amenities.query.all()
    if form.validate_on_submit():
        reservation = Reservation(room_id=form.confirm.data, group_id=0, building_id=2, user_id=current_user.id, totalHours=2)
        db.session.add(reservation)
        db.session.commit()
        return redirect(url_for('confirmation'))
    return render_template('birdLibrary.html', title='Bird Library', form=form, rooms=rooms, amens=amens)


@app.route("/lifeScienceBuilding", methods=['GET', 'POST'])
@login_required
def lifeScienceBuilding():
    form = BuildingForm()
    rooms = Room.query.filter_by(building_id='3').all()
    amens = Amenities.query.all()
    if form.validate_on_submit():
        reservation = Reservation(room_id=form.confirm.data, group_id=0, building_id=3, user_id=current_user.id, totalHours=2)
        db.session.add(reservation)
        db.session.commit()
        return redirect(url_for('confirmation'))
    return render_template('lifeScienceBuilding.html', title='Life Science Building', form=form, rooms=rooms, amens=amens)


#@app.route("/link", methods=['GET', 'POST'])
#@login_required
#def link():
    #form = BuildingForm()
    #rooms = Room.query.filter_by(building_id='6').all()
    #amens = Amenities.query.all()
    #return render_template('link.html', title='Link', form=form, rooms=rooms, amens=amens)


@app.route("/falk", methods=['GET', 'POST'])
@login_required
def falk():
    form = BuildingForm()
    rooms = Room.query.filter_by(building_id='5').all()
    amens = Amenities.query.all()
    if form.validate_on_submit():
        reservation = Reservation(room_id=form.confirm.data, group_id=0, building_id=5, user_id=current_user.id, totalHours=2)
        db.session.add(reservation)
        db.session.commit()
        return redirect(url_for('confirmation'))
    return render_template('falk.html', title='Falk', form=form, rooms=rooms, amens=amens)


@app.route("/newhouse", methods=['GET', 'POST'])
@login_required
def newhouse():
    form = BuildingForm()
    rooms = Room.query.filter_by(building_id='4').all()
    amens = Amenities.query.all()
    return render_template('newhouse.html', title='Newhouse', form=form, rooms=rooms, amens=amens)


@app.route("/whitman", methods=['GET', 'POST'])
@login_required
def whitman():
    form = BuildingForm()
    rooms = Room.query.filter_by(building_id='1').all()
    amens = Amenities.query.all()
    if form.validate_on_submit():
        reservation = Reservation(room_id=form.confirm.data, group_id=0, building_id=1, user_id=current_user.id, totalHours=2)
        db.session.add(reservation)
        db.session.commit()
        return redirect(url_for('confirmation'))
    return render_template('whitman.html', title='Whitman', form=form, rooms=rooms, amens=amens)


@app.route("/confirmation")
@login_required
def confirmation():
    return render_template('confirmation.html', title='Confirm Room')


