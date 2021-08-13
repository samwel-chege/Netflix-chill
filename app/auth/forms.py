from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms import validators
from wtforms.validators import Required,Email,EqualTo
from ..model import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators = [Required()])
    username = StringField('Enter your username', validators = [Required()])
    password = PasswordField('Password', validators = [Required(), EqualTo('password_confirm', message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit  = SubmitField('Sign up')

    def validate_username(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

            '''
            function that in the data field and checks the database to confirm there is no user registered with the same email address
            '''

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')   
            
            '''
            function that checks to see if the useraname is unique  and raises a validate error if another user with a similar username is found 
            '''

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()]) 
    password = PasswordField('Password',validators=[Required()])   
    remember = BooleanField('Remember me')    
    submit = SubmitField('Sign In')    