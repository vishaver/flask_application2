from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo
from wtforms import ValidationError
from myproject.models import User

class LoginForm(FlaskForm):
    username = StringField("Enter the username:",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Log In")

class RegistrationForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired(),EqualTo('pass_confirm',message='Password must match')])
    pass_confirm = PasswordField("Confirm Password",validators=[DataRequired()])
    submit = SubmitField("Register")

    def check_user(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username is already registered')
