from flask.ext.wtf import Form
from wtforms import StringField, SelectField, TextAreaField, DateTimeField, BooleanField, TextAreaField, PasswordField, IntegerField, validators, SubmitField
from wtforms.validators import DataRequired, Length, IPAddress, MacAddress, Optional

class NewAlertForm(Form):
	alert_title = StringField('Title',validators=[DataRequired()])
	alert_type = StringField('Type',validators=[DataRequired()])
	alert_ip = StringField('IP Address',validators=[Optional(),IPAddress("Bad IP Address")])
	alert_mac = StringField('MAC Address',validators=[Optional(), MacAddress("Bad Mac Address")])
	alert_comments = TextAreaField('Comments')
	

class UpdateAlertForm(Form):
        alert_status = SelectField('Status', choices=[('',''),('Resolved','Resolved'),('Updated','Updated')])
        alert_type = StringField('Type')
        alert_ip = StringField('IP Address',validators=[Optional(),IPAddress("Bad IP Address")])
        alert_mac = StringField('MAC Address',validators=[Optional(), MacAddress("Bad Mac Address")])
        alert_comments = TextAreaField('Comments')

class IncidentForm(Form):
	incident_name = StringField('incident_name', validators=[DataRequired()])
	incident_value = StringField('incident_value', validators=[DataRequired()])
	incident_status = SelectField('incident_status', choices = [('manual','Manual'),('linked','Linked')])
	incident_comments = TextAreaField('incident_comments')


