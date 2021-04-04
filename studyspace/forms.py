from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, BooleanField

from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField

from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

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
    group = RadioField('Choose preferred study method', choices=[('Group'), ('Solo')])
    submit = SubmitField('Submit')

class BuildingForm(FlaskForm):
    name = StringField('Room Name: ')
    amenities = StringField('Amenities: ')
    floor = StringField('Floor: ')
    roomType = StringField('Room Type: ')
    capacity = StringField('Room Capacity: ')
    confirm = StringField('Confirm Room by Entering Room Number: ',
                            validators=[DataRequired()])
    confirmButton = SubmitField('Confirm')

    def validate_confirmation(self, confirm):
        reservation = Reservation.query.filter_by(room_id=confirm.data).first()
        if reservation:
            raise ValidationError('This room has already been reserved. Please select another room.')



