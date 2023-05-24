# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf          import FlaskForm
from flask_wtf.file     import FileField, FileRequired
from wtforms            import StringField, TextAreaField, SubmitField, PasswordField, FloatField
from wtforms.validators import InputRequired, Email, DataRequired

class LoginForm(FlaskForm):
	username    = StringField  (u'Username'  , validators=[DataRequired()])
	password    = PasswordField(u'Password'  , validators=[DataRequired()])

class RegisterForm(FlaskForm):
	name        = StringField  (u'Name'      )
	username    = StringField  (u'Username'  , validators=[DataRequired()])
	password    = PasswordField(u'Password'  , validators=[DataRequired()])
	email       = StringField  (u'Email'     , validators=[DataRequired(), Email()])

class OrdersForm(FlaskForm):
    name = 		 	  StringField('Name')
    terminal_id = 	  StringField('Terminal ID')
    port_id = 		  StringField('Port ID')
    client_longitud = FloatField('Client Longitude')
    client_latitud =  FloatField('Client Latitude')
    client_name = 	  StringField('Client Name')
    client_vat = 	  StringField('Client VAT')
    client_address =  StringField('Client Address')
    submit = 	      SubmitField('Submit')


