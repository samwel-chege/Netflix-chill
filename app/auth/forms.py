from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms import validators
from wtforms.validators import Required,Email,EqualTo
from ..model import User

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators = [Required()])
    password = PasswordField('Password', validators = [Required(), EqualTo('password_confirm', message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit  = SubmitField('Sign up')