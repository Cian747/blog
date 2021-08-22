from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Email, Required


class BlogForm(FlaskForm):

 title = StringField('Blog title',validators=[Required()])

 author = StringField('Name',validators=[Required()])

 blog = TextAreaField('Write blog here: ')

 submit = SubmitField('Submit')



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment',validators=[Required()])
    submit = SubmitField('Submit')


class SubscriptionForm(FlaskForm):
    email = StringField('Email',validators=[Required(),Email()])
    submit = SubmitField('Submit')
