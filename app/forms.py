from flask.ext.wtf import Form
from wtforms import StringField, SelectField, TextAreaField, BooleanField, TextAreaField, PasswordField, IntegerField, validators
from wtforms.validators import DataRequired, Length

class AlertForm(Form):
	alert_name = StringField('alert_name',validators=[DataRequired()])
 	alert_value = StringField('alert_value',validators=[DataRequired()])
	alert_status = SelectField('alert_status', choices=[('new','New'),('Res','Resolved'),('prom','Promoted')])
	alert_comments = TextAreaField('alert_comments')
