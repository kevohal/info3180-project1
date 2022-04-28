from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, IntegerField, DecimalField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length


class AddPropertyForm(FlaskForm):

    title = StringField('Property Title', validators = [InputRequired('Property Title is required!'), Length(min= 1, max=255)])
    description = TextAreaField('Description of Property', validators=[InputRequired()])
    rooms = IntegerField('No. of Rooms', validators = [InputRequired(), Length(max=3 )])
    baths = DecimalField('No. of Bathrooms', validators=[InputRequired()], places=2)
    price = DecimalField('Price', validators=[InputRequired()], places=2)
    type = SelectField('Property Type', choices=[('Apartment', 'Apartment'), ('House', 'House')], validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileAllowed(['jpg', 'jpeg', 'png'], 'Images Only!'), FileRequired('Photo of property is required')])