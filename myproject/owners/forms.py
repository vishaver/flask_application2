from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,DateTimeField,RadioField,SelectField,TextAreaField,TextField,IntegerField
from wtforms.validators import DataRequired,Email,EqualTo, Length, ValidationError

class Addowner(FlaskForm):
    name = StringField("Name of owner:",validators=[DataRequired()])
    puppy_id = IntegerField("Enter Puppy Id:",validators=[DataRequired()])
    submit = SubmitField("Submit")