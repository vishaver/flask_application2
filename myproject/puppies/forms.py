from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,DateTimeField,RadioField,SelectField,TextAreaField,TextField,IntegerField
from wtforms.validators import DataRequired,Email,EqualTo, Length, ValidationError



class Add(FlaskForm):
    name = StringField("Name of pupy",validators=[DataRequired()])
    submit = SubmitField("Submit")

class Del(FlaskForm):
    id = IntegerField("Enter the id:",validators=[DataRequired()])
    submit = SubmitField("Submit")

