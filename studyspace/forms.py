from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, BooleanField

from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField

from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired

from studyspace.database import User, Reservation

#username length is being capped at 20 characters, minimum of 3
#password length has a maximum of 20 characters, minimum of 8
#these classes import flask libraries and accept emails, usernames, passwords etc.

#form for createAccount.html file
class RegistrationForm(FlaskForm):
    #email must have some text inputted to field and must be at least 0 and at most 50 characters to validate.
    email = StringField('Email', 
                            validators=[DataRequired(), Length(min=0, max=50),Email()])
    #password must have some text inputted to field and must be at least 8 and at most 20 characters to validate.
    password = PasswordField('Password',
                                validators=[DataRequired(), Length(min=8, max=20)])
    #EqualTo confirms that the passwword and the confirm_password are the same
    confirm_password = PasswordField('Confirm Password',
                                        validators=[DataRequired(), EqualTo('password')])
    #submit button that creates the account
    submit = SubmitField('Create Account')

    #function that determines if email inputted already exists in database
    def validate_email(self, email):
        user = User.query.filter_by(emailAddress=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

#form for login.html
class LoginForm(FlaskForm):
    #email must have some text inputted to field and must be at least 0 and at most 50 characters to validate.
    email = StringField('Email', 
                            validators=[DataRequired(), Length(min=0, max=50), Email()])
    #password must have some text inputted to field and must be at least 8 and at most 20 characters to validate.
    password = PasswordField('Password',
                                validators=[DataRequired(), Length(min=8, max=20)])
    #button for if the user wants their login information to preload for them on next use
    remember = BooleanField('Remember Me')
    #submit button that logs user in
    submit = SubmitField('Login')


#form for the survey.html and newSurvey.html file
class SurveyForm(FlaskForm):
    #field for user to enter the course they desire to study, only requirement is the field has some input
    course = StringField('Course you want to study', validators=[DataRequired()])

    #radio buttons for user to choose their preferred method of study
    group = RadioField('Choose preferred study method', choices=[('Group'), ('Solo')], validators=[InputRequired()])
    #submit button submits data from survey to database
    submit = SubmitField('Submit')

class BuildingForm(FlaskForm):
    name = StringField('Room Name: ')
    amenities = StringField('Amenities: ')
    floor = StringField('Floor: ')
    roomType = StringField('Room Type: ')
    capacity = StringField('Room Capacity: ')
    #confirm demands a string input that will be the number for the room being reserved
    confirm = StringField('Confirm Room by Entering Room Number: ',
                            validators=[DataRequired()])
    #confirmation button for confirming after inputting room number
    confirmButton = SubmitField('Confirm')

    #Not functional but also doesn't impact running
    #Would have checked if the room had already been reserved in the database and raised an error if it had
    def validate_reserve(self, confirm):
        reservation = Reservation.query.filter_by(room_id=confirm.data)
        if reservation:
            raise ValidationError('Sorry, that room is already reserved. Please choose a new one.')
    #Not functional but also doesn't impact running
    #Would have checked if the room number was registered to a room in the database and would've raised an error if not
    def validate_room(self, name, confirm):
        if confirm.data != name.data:
            raise ValidationError('That room number does not match. Please enter the correct room number for this room.')

#takes in the room number for the reservation being cancelled
class cancelReservation(FlaskForm):
    name = StringField('Room Number: ',
                            validators=[DataRequired()])
    #confirmation button for cancelling reservation
    confirm = SubmitField('Cancel Reservation')



