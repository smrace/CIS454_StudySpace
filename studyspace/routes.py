from flask import render_template, url_for, flash, redirect, request
from studyspace import app, db, bcrypt
from studyspace.forms import RegistrationForm, LoginForm, SurveyForm, BuildingForm, cancelReservation
from studyspace.database import User, Building, Group, Room, Amenities, Subject, Reservation
from flask_login import login_user, current_user, logout_user, login_required

#define the home page as mainPage.html
@app.route("/")
@app.route("/home")
def home():
    return render_template('mainPage.html')



#define the route to createAccount.html
@app.route("/createAccount", methods=['GET', 'POST'])
def createAccount():
    #check if new user info is valid
    if current_user.is_authenticated:
        #move user to new account survey
        return redirect(url_for('newSurvey'))
    #sets the form of this route to the registration form from forms.py
    form = RegistrationForm()
    #check if validators pass when the submit button is clicked
    if form.validate_on_submit():
        #create a hashed pass using bcrypt package
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
         #add user and their info to database
        user = User(emailAddress=form.email.data, password=hashed_password)
        db.session.add(user)
        #update database
        db.session.commit()
        flash(f'Account successfully created!', 'success')
        #move user to the new account survey
        return redirect(url_for('newSurvey'))
    return render_template('createAccount.html', title='Create Account', form=form)



#see forms.py for more info on LoginForm() and RegistrationForm()
#define the route to login.html
@app.route("/login", methods=['GET', 'POST'])
def login():
    #check if user info is valid
    if current_user.is_authenticated:
         #move user to returning account survey
        return redirect(url_for('survey'))
    #set the form to the login form from forms.py
    form = LoginForm()
    #check if validators pass when the submit button is clicked
    if form.validate_on_submit():
        #find the user by filtering the database with a query
        user = User.query.filter_by(emailAddress=form.email.data).first()
        #authenticates user password
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            #move the user to returning account survey
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

#define the route to mainPage.html
@app.route("/mainPage")
def mainPage():
    return render_template('mainPage.html', title='Main Page')

#define the route to map.html
@app.route("/map", methods=['GET', 'POST'])
def map():
    return render_template('map.html', title='Map')

#define the route to survey.html
@app.route("/survey", methods=['GET', 'POST'])
def survey():
    #sets the form to the survey form from forms.py
    form = SurveyForm()
     #define a validator to check if the course inputted matches an element of a preset list
    def validate_course():
        exists = False
        #list of courses
        classes = ['MAT 101', 'ENG 101', 'SCI 101', 'GEO 101']
        #loop through courses
        for p in classes:
             #check at each element to see if it equals the input
            if(form.course.data == p):
                exists = True
         #return true if it matches one and false if it doesn't
        if(exists != True):
            return False
        else:
            return True
    #check validations when the submit button is clicked
    if form.validate_on_submit():
        #check the return value of validate_course
        if validate_course():
            #update user information if true
            current_user.study = form.course.data
            #update database with changes
            db.session.commit()
            return redirect(url_for('map'))
        else:
            #if it doesnt exist, tell user to try inputting class again and don't move forward
            flash('Invalid Class, try again.' , 'danger')
    return render_template('survey.html', title='Survey', form=form)

#define route for newSurvey.html
@app.route("/newSurvey", methods=['GET', 'POST'])
def newSurvey():
    #sets the form to the survey form from forms.py
    form = SurveyForm()
    #define a validator to check if the course inputted matches an element of a preset list
    def validate_course():
        exists = False
        #list of courses
        classes = ['MAT 101', 'ENG 101', 'SCI 101', 'GEO 101']
        #loop through courses
        for p in classes:
            #check at each element to see if it equals the input
            if(form.course.data == p):
                exists = True
        #return true if it matches one and false if it doesn't
        if(exists != True):
            return False
        else:
            return True
    #check validations when the submit button is clicked
    if form.validate_on_submit():
        #check the return value of validate_course
        if validate_course():
            #update user information if true
            current_user.study = form.course.data
            #update database with changes
            db.session.commit()
            #move user to map.html
            return redirect(url_for('map'))
        else:
            #if it doesnt exist, tell user to try inputting class again and don't move forward
            flash('Invalid Class, try again.' , 'danger')
    return render_template('newSurvey.html', title='New Account Survey', form=form)

#define route for about.html
@app.route("/about")
def about():
    return render_template('about.html', title='about')

#define route for findGroup.html
@app.route("/findGroup")
@login_required
def findGroup():
    myUser = User.query.all()
    return render_template('findGroup.html', title='Find Group', myUser=myUser)


#all builing routes are the same except for their building id's
#all comments apply to each subsequent building route
#define route for birdLibrary.html
@app.route("/birdLibrary", methods=['GET', 'POST'])
#user needs to be logged in
@login_required
def birdLibrary():
    #takes form from forms.py
    form = BuildingForm()
    #gets all rooms for the building from the database
    rooms = Room.query.filter_by(building_id='2').all()
    #gets all amenites for each room from the database
    amens = Amenities.query.all()
    if form.validate_on_submit():
        #if the form is submitted correctly the room reservation is created and the database is updated
        reservation = Reservation(room_id=form.confirm.data, group_id=0, building_id=2, user_id=current_user.id, totalHours=2)
        db.session.add(reservation)
        db.session.commit()
        #redirected to the confirmation page in case the user wishes to cancel their reservation
        return redirect(url_for('confirmation'))
    return render_template('birdLibrary.html', title='Bird Library', form=form, rooms=rooms, amens=amens)

#define route for lifeScienceBuilding.html
@app.route("/lifeScienceBuilding", methods=['GET', 'POST'])
@login_required
def lifeScienceBuilding():
    #set the form to the building form in forms.py
    form = BuildingForm()
    #filter through rooms with a query to find the ones with building_id=3
    rooms = Room.query.filter_by(building_id='3').all()
    #filter to find the amenities with a query
    amens = Amenities.query.all()
    if form.validate_on_submit():
        reservation = Reservation(room_id=form.confirm.data, group_id=0, building_id=3, user_id=current_user.id, totalHours=2)
        db.session.add(reservation)
        db.session.commit()
        return redirect(url_for('confirmation'))
    return render_template('lifeScienceBuilding.html', title='Life Science Building', form=form, rooms=rooms, amens=amens)


#define route for falk.html
@app.route("/falk", methods=['GET', 'POST'])
@login_required
def falk():
    #set the form to the building form in forms.py
    form = BuildingForm()
    #filter through rooms with a query to find the ones with building_id=5
    rooms = Room.query.filter_by(building_id='5').all()
    #filter to find the amenities with a query
    amens = Amenities.query.all()
    if form.validate_on_submit():
        reservation = Reservation(room_id=form.confirm.data, group_id=0, building_id=5, user_id=current_user.id, totalHours=2)
        db.session.add(reservation)
        db.session.commit()
        return redirect(url_for('confirmation'))
    return render_template('falk.html', title='Falk', form=form, rooms=rooms, amens=amens)

#define route for newhouse.html
@app.route("/newhouse", methods=['GET', 'POST'])
@login_required
def newhouse():
    #set the form to the building form in forms.py
    form = BuildingForm()
    #filter through rooms with a query to find the ones with building_id=4
    rooms = Room.query.filter_by(building_id='4').all()
    #filter to find the amenities with a query
    amens = Amenities.query.all()
    if form.validate_on_submit():
        reservation = Reservation(room_id=form.confirm.data, group_id=0, building_id=4, user_id=current_user.id, totalHours=2)
        db.session.add(reservation)
        db.session.commit()
        return redirect(url_for('confirmation'))
    return render_template('newhouse.html', title='Newhouse', form=form, rooms=rooms, amens=amens)

#define route for whitman.html
@app.route("/whitman", methods=['GET', 'POST'])
@login_required
def whitman():
    #set the form to the building form in forms.py
    form = BuildingForm()
    #filter through rooms with a query to find the ones with building_id=1
    rooms = Room.query.filter_by(building_id='1').all()
    #filter to find the amenities with a query
    amens = Amenities.query.all()
    if form.validate_on_submit():
        reservation = Reservation(room_id=form.confirm.data, group_id=0, building_id=1, user_id=current_user.id, totalHours=2)
        db.session.add(reservation)
        db.session.commit()
        return redirect(url_for('confirmation'))
    return render_template('whitman.html', title='Whitman', form=form, rooms=rooms, amens=amens)



#this function would have had a portion to check if the room number entered was registered to an actual room in the database
#would have also checked if there was a registration for that room but we were not able to implement these in the time frame for this project
#define route for confirmation.html
@app.route("/confirmation", methods=['GET', 'POST'])
#login needed for access to this page
@login_required
def confirmation():
    #gets form from forms.py
    form = cancelReservation()
    #queries the databse for all of the rooms
    rooms = Room.query.all()
    #if the form is submitted correctly
    if form.validate_on_submit():
        #cancels the reservation
        #currently this is not fully functional, thus the delete and commit are commented out
        reservation = Reservation.query.filter_by(room_id=form.name.data)
        #db.session.delete(reservation)
        #db.session.commit()
        #would redirect to main page if functional
        return redirect(url_for('map'))
    return render_template('confirmation.html', title='Confirm Room', form=form, rooms=rooms)


