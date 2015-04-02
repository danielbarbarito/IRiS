from flask import render_template, redirect, url_for
from app import app
from forms import AlertForm
from models import Alert, iris_db

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
