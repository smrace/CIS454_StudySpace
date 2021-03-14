from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#username length is being capped at 20 characters, minimum of 4
#password length has a maximum of 20 characters, minimum of 5
#these classes import flask libraries and accept emails, usernames, passwords etc.
class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                                validators=[DataRequired(), Length(min=5, max=20)])
    #EqualTo confirms that the passwword and the confirm_password are the same
    confirm_password = PasswordField('Confirm Password',
                                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')

class LoginForm(FlaskForm):
    email = StringField('Email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                                validators=[DataRequired(), Length(min=5, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

