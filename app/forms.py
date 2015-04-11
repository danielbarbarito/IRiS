from flask.ext.wtf import Form
from wtforms import StringField, SelectField, TextAreaField, DateTimeField, BooleanField, TextAreaField, PasswordField, IntegerField, validators, SubmitField
from wtforms.validators import DataRequired, Length, IPAddress, MacAddress, Optional

class NewAlertForm(Form):
	title = StringField('Title',validators=[DataRequired()])
	atype = StringField('Type',validators=[DataRequired()])
	ip = StringField('IP Address',validators=[Optional(),IPAddress("Bad IP Address")])
	mac = StringField('MAC Address',validators=[Optional(), MacAddress("Bad Mac Address")])
	comments = TextAreaField('Comments')
	

class UpdateAlertForm(Form):
        status = SelectField('Status', choices=[('',''),('Resolved','Resolved'),('Updated','Updated')])
        atype = StringField('Type')
        ip = StringField('IP Address',validators=[Optional(),IPAddress("Bad IP Address")])
        mac = StringField('MAC Address',validators=[Optional(), MacAddress("Bad Mac Address")])
        comments = TextAreaField('Comments')

class NewIncidentForm(Form):
	title = StringField('Title',validators=[DataRequired()])
	itype = StringField('Type', choices=[('User','User'),('Policy','Policy'),('Network','Network')], validators=[DataRequired()])
	#ip = StringField('IP Address',validators=[Optional(),IPAddress("Bad IP Address")])
	#mac = StringField('MAC Address',validators=[Optional(), MacAddress("Bad Mac Address")])
	comments = TextAreaField('Comments')

class UpdateIncidentForm(Form):
	#status = SelectField('Status', choices=[('',''),('Resolved','Resolved'),('Updated','Updated')])
	status = SelectField('Status', choices=[('',''),('Manual','Manual'),('Promoted','Promoted')])
	itype = StringField('Type', choices=[('User','User'),('Policy','Policy'),('Network','Network')])
	#ip = StringField('IP Address',validators=[Optional(),IPAddress("Bad IP Address")])
	#mac = StringField('MAC Address',validators=[Optional(), MacAddress("Bad Mac Address")])
	comments = TextAreaField('Comments')


		
