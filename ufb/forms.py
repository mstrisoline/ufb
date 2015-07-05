#Single File to manage all forms generated via WTF Forms and their validation
#Most of these should be very self explanitory

from flask.ext.wtf import Form
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from wtforms import fields
from wtforms.validators import Email, InputRequired, ValidationError, Length

from .models import *

class LoginForm(Form):
    email = fields.StringField(validators=[InputRequired(), Email()])
    password =  fields.PasswordField(validators=[InputRequired()])

    def validate_password(form, field):
        try:
            user = User.query.filter(User.email == form.email.data).one()
        except (MultipleResultsFound, NoResultFound):
            raise ValidationError("Invalid user")
        if user is None:
            raise ValidationError("Invalid user")
        if not user.validate_pw(form.password.data):
            raise ValidationError("Invalid password")
        form.user = user

class RegisterForm(Form):
    first = fields.StringField("First Name", validators=[InputRequired()])
    last = fields.StringField("Last Name", validators=[InputRequired()])
    nickname = fields.StringField("Nickname", validators=[InputRequired()])
    email = fields.StringField("Email", validators=[InputRequired()])
    password = fields.PasswordField("Password", validators=[InputRequired()])

    def validate_email(form, field):
        user = User.query.filter(User.email == field.data).first()
        nickname = User.query.filter(User.nickname == field.data).first()
        if user and nickname is not None:
            raise ValidationError("Email is already registered")

#Place Holder for Generating a Profile Form
class ProfileForm(Form):
    pass
    
class PostForm(Form):
    post_body = fields.TextAreaField("Post Something", validators=[Length(min=1, max=254, message="Maximum Length is 254 Characters")])
    #This is to create a individual form submit rather than an entire page
    submit = fields.SubmitField('Submit New Post')

class ReplyForm(Form):
    reply_body = fields.TextAreaField("Reply to Post", validators=[Length(min=1, max=254, message="Maximum Length is 254 Characters")])
    #This is to create a individual form submit rather than an entire page
    submit = fields.SubmitField('Reply to post')
