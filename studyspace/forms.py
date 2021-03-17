from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from studyspace.database import User
#username length is being capped at 20 characters, minimum of 3
#password length has a maximum of 20 characters, minimum of 8
#these classes import flask libraries and accept emails, usernames, passwords etc.
class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                                validators=[DataRequired(), Length(min=8, max=20)])
    #EqualTo confirms that the passwword and the confirm_password are the same
    confirm_password = PasswordField('Confirm Password',
                                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please enter a new one!')
    def validate_email(self, emailAddress):
        user = User.query.filter_by(emailAddress=emailAddress.data).first()
        if user:
            raise ValidationError('Email already exists. Please enter a new one!')

class LoginForm(FlaskForm):
    email = StringField('Email', 
                            validators=[DataRequired(), Length(min=0, max=50), Email()])
    password = PasswordField('Password',
                                validators=[DataRequired(), Length(min=8, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

