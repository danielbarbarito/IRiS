from flask.ext.wtf import Form
from wtforms import StringField, SelectField, TextAreaField, BooleanField, TextAreaField, PasswordField, IntegerField, validators
from wtforms.validators import DataRequired, Length

class AlertForm(Form):
	alert_name = StringField('alert_name',validators=[DataRequired()])
 	alert_value = StringField('alert_value',validators=[DataRequired()])
	alert_status = SelectField('alert_status', choices=[('new','New'),('Res','Resolved'),('prom','Promoted')])
	alert_comments = TextAreaField('alert_comments')

class IncidentForm(Form):
	incident_name = StringField('incident_name', validators=[DataRequired()])
	incident_value = StringField('incident_value', validators=[DataRequired()])
	incident_status = SelectField('incident_status', choices = [('manual','Manual'),('linked','Linked')])
	incident_comments = TextAreaField('incident_comments')
