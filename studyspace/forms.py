from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, BooleanField

from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField

from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired

from studyspace.database import User, Reservation

#username length is being capped at 20 characters, minimum of 3
#password length has a maximum of 20 characters, minimum of 8
#these classes import flask libraries and accept emails, usernames, passwords etc.
class RegistrationForm(FlaskForm):
    email = StringField('Email', 
                            validators=[DataRequired(), Length(min=0, max=50),Email()])
    password = PasswordField('Password',
                                validators=[DataRequired(), Length(min=8, max=20)])
    #EqualTo confirms that the passwword and the confirm_password are the same
    confirm_password = PasswordField('Confirm Password',
                                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')

    def validate_email(self, email):
        user = User.query.filter_by(emailAddress=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', 
                            validators=[DataRequired(), Length(min=0, max=50), Email()])
    password = PasswordField('Password',
                                validators=[DataRequired(), Length(min=8, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



class SurveyForm(FlaskForm):
    course = StringField('Course you want to study', validators=[DataRequired()])
    group = RadioField('Choose preferred study method', choices=[('Group'), ('Solo')], validators=[InputRequired()])
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



