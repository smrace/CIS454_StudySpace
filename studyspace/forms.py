from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, BooleanField

from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField

from wtforms.validators import DataRequired, Length, Email, EqualTo

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

class LoginForm(FlaskForm):
    email = StringField('Email', 
                            validators=[DataRequired(), Length(min=0, max=50), Email()])
    password = PasswordField('Password',
                                validators=[DataRequired(), Length(min=8, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

def validate_course(form, field):
    exists = False
    classes = ['MAT 101', 'ENG 101', 'SCI 101', 'GEO 101']
    for p in classes:
        if(field.data == p):
            exists = True
    if(exists != True):
        raise ValidationError('Class does not exist, please enter an existing class.')

class SurveyForm(FlaskForm):
    course = StringField('Course you want to study', validators=[DataRequired(), validate_course])
    group = RadioField('Choose preferred study method', choices=[('Group'), ('Solo')])
    submit = SubmitField('Submit')