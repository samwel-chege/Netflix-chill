from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('REview title', validators = [Required()])
    review = TextAreaField('Movie review', validators= [Required()])
    submit = SubmitField('submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators= [Required])
    submit = SubmitField('Submit')
  