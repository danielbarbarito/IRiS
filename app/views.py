from flask import render_template, redirect, url_for
from app import app
from forms import AlertForm, IncidentForm
from models import Alert, Incident, iris_db

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html",
				title='Home')


@app.route('/alert', methods=['GET', 'POST'])
def alert():
	form = AlertForm()
	#mongoalchemy
        #alerts = session.query(Alert).filter(Alert.alert_name == 'Second_Alert')       
        alerts = iris_db.query(Alert)
	
	if form.validate_on_submit():
		alert_name = form.alert_name.data
		alert_value = form.alert_value.data
		alert_status = form.alert_status.data
		alert_comments = form.alert_comments.data
		#mongoalchemy
		iris_db.insert(Alert(alert_name=alert_name,alert_value=alert_value,alert_status=alert_status,alert_comments=alert_comments))
		return redirect(url_for('alert'))
	return render_template('alert.html', 
				title='Alert',
				alerts=alerts,
				form=form)

@app.route('/incident', methods=['GET', 'POST'])
def incident():
	form = IncidentForm()
	incidents = iris_db.query(Incident)

	if form.validate_on_submit():
		incident_name = form.incident_name.data
		incident_value = form.incident_value.data
		incident_status = form.incident_status.data
		incident_comments = form.incident_comments.data

		iris_db.insert(Incident(incident_name=incident_name, incident_value=incident_value, incident_status=incident_status, incident_comments=incident_comments))
		return redirect(url_for('incident'))
	return render_template('incident.html',
				title='Incident',
				incidents=incidents,
				form=form)
