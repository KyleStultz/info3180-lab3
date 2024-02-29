from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
	
	name = StringField('Name', validators=[InputRequired()])
	email = EmailField('E-mail', validators=[InputRequired(),])
	subject = StringField('Subject', validators=[InputRequired()])
	message = TextAreaField('Message', validators=[InputRequired()])