from flask import render_template, redirect, url_for, request
from datetime import datetime
from app import app
from forms import NewAlertForm, UpdateAlertForm, NewIncidentForm, UpdateIncidentForm
from models import Alert, Incident, iris_db

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html",
				title='Home')


@app.route('/alert', methods=['GET', 'POST'])
def alert():

	alerts = iris_db.query(Alert)
	incident_alerts = []

	if request.method == 'POST':
		if request.form['btn'] == 'New':
			return redirect(url_for('new_alert'))
		elif request.form['btn'] == 'Update':
			selected = request.form.getlist('selected')
			return redirect(url_for('update_alert', selected=selected))
		elif request.form['btn'] == 'Promote':
			selected = request.form.getlist('selected')
			for s in selected:
				query = iris_db.query(Alert).filter(Alert.alert_title == s)
				for q in query:
					incident_alerts.append(q.to_ref())				
					#iris_db.remove(q)

			
			iris_db.insert(Incident(
				incident_title=q.alert_title,
				incident_ip=q.alert_ip,
				incident_mac=q.alert_mac,
				incident_entered=q.alert_entered,
				incident_comments=q.alert_comments,
				incident_status="Promoted",
				incident_type=q.alert_type,
				incident_alerts=incident_alerts
				))
	
	return render_template('alert.html', 
				title='Alert',
				alerts=alerts)


@app.route('/new_alert', methods=['GET', 'POST'])
def new_alert():
	form = NewAlertForm()
        #mongoalchemy
        #alerts = session.query(Alert).filter(Alert.alert_name == 'Second_Alert')       
	new = 'New'
	if form.validate_on_submit():
                alert_title = form.alert_title.data
                alert_ip = [form.alert_ip.data]
                alert_mac = [form.alert_mac.data]
                alert_type = [form.alert_type.data]
                alert_entered = datetime.utcnow()
                alert_comments = [form.alert_comments.data]
		
		print alert_title
                #mongoalchemy
                iris_db.insert(Alert(alert_title=alert_title,
                                        alert_ip=alert_ip,
                                        alert_mac=alert_mac,
                                        alert_status=new,
                                        alert_type=alert_type,
                                        alert_comments=alert_comments,
                                        alert_entered=alert_entered))
                return redirect(url_for('alert'))


        return render_template("new_alert.html",
                                title='New Alert',
				form=form)

@app.route('/update_alert', methods=['GET', 'POST'])
def update_alert():
	alerts = []
	form= UpdateAlertForm()

	selected = request.args.getlist('selected')
	print selected
	for s in selected:
		query = iris_db.query(Alert).filter(Alert.alert_title == s)
		for q in query:
			d = {
				'alert_title':q.alert_title,
				'alert_status':q.alert_status,
				'alert_type':q.alert_type,
				'alert_ip':q.alert_ip,
				'alert_mac':q.alert_mac,
				'alert_entered':q.alert_entered,
				'alert_comments':q.alert_comments,
				}
		alerts.append(d)

	if request.method == 'POST':
		update = request.form.getlist('update')
	
		if update:
		
			alert = iris_db.query(Alert).filter(Alert.alert_title == update[0])
			if form.validate_on_submit():
	    	        	alert_ip = form.alert_ip.data
        		        alert_mac = form.alert_mac.data
				alert_type = form.alert_type.data
		                alert_comments = form.alert_comments.data
				alert_status = form.alert_status.data
			
				if alert_status != '':
                                        alert.set(Alert.alert_status,alert_status).execute()

				if alert_type != '':
                                        alert.extend(Alert.alert_type,alert_type).execute()

				if alert_ip != '':
					alert.extend(Alert.alert_ip,alert_ip).execute()
				
				if alert_mac != '':
                                        alert.extend(Alert.alert_mac,alert_mac).execute()

				if alert_comments != '':
                                        alert.extend(Alert.alert_comments,alert_comments).execute()
		
				alerts = iris_db.query(Alert)	
				#fix boxes not clearing
				return render_template("update_alert.html",
			                                title='Update Alert',
                        			        form=form,
			                                alerts=alerts)
	return render_template("update_alert.html",
                                title='Update Alert',
				form=form,
				alerts=alerts)

@app.route('/incident', methods=['GET', 'POST'])
def incident():
	
	incidents = iris_db.query(Incident)

	if request.method == 'POST':
		if request.form['btn'] == 'New':
			return redirect(url_for('new_incident'))
		elif request.form['btn'] == 'Update':
			selected = request.form.getlist('selected')
			return redirect(url_for('update_incident', selected=selected))
	
	return render_template('incident.html', 
				title='Incident',
				incidents=incidents)


		#return redirect(url_for('incident'))
	#return render_template('incident.html',
	#			title='Incident',
	#			incidents=incidents,
	#			form=form)

@app.route('/new_incident', methods=['GET', 'POST'])
def new_incident():
	form = NewIncidentForm()
        #mongoalchemy
        #alerts = session.query(Alert).filter(Alert.alert_name == 'Second_Alert')       
	if form.validate_on_submit():
                incident_title = form.incident_title.data
                incident_ip = [form.incident_ip.data]
                incident_mac = [form.incident_mac.data]
                incident_type = [form.incident_type.data]
                incident_entered = datetime.utcnow()
                incident_comments = [form.incident_comments.data]
		incident_alerts = []

				
                #mongoalchemy
                iris_db.insert(Incident(incident_title=incident_title,
                                        incident_ip=incident_ip,
                                        incident_mac=incident_mac,
                                        incident_status="Manual",
                                        incident_type=incident_type,
                                        incident_comments=incident_comments,
                                        incident_entered=incident_entered,
					incident_alerts=incident_alerts)
					)
                return redirect(url_for('incident'))


        return render_template("new_incident.html",
                                title='New Incident',
				form=form)

@app.route('/update_incident', methods=['GET', 'POST'])
def update_incident():
	incidents = []
	form= UpdateIncidentForm()

	selected = request.args.getlist('selected')
	print selected
	for s in selected:
		query = iris_db.query(Incident).filter(Incident.incident_title == s)
		for q in query:
			d = {
				'incident_title':q.incident_title,
				'incident_status':q.incident_status,
				'incident_type':q.incident_type,
				'incident_ip':q.incident_ip,
				'incident_mac':q.incident_mac,
				'incident_entered':q.incident_entered,
				'incident_comments':q.incident_comments,
				}
		incidents.append(d)

	if request.method == 'POST':
		update = request.form.getlist('update')
	
		if update:
		
			incident = iris_db.query(Incident).filter(Incident.incident_title == update[0])
			if form.validate_on_submit():
	    	        	incident_ip = form.incident_ip.data
        		        incident_mac = form.incident_mac.data
				incident_type = form.incident_type.data
		                incident_comments = form.incident_comments.data
				incident_status = form.incident_status.data
			
				if incident_status != '':
                                        incident.set(Incident.incident_status,incident_status).execute()

				if incident_type != '':
                                        incident.extend(Incident.incident_type,incident_type).execute()

				if incident_ip != '':
					incident.extend(Incident.incident_ip,incident_ip).execute()
				
				if incident_mac != '':
                                        incident.extend(Incident.incident_mac,incident_mac).execute()

				if incident_comments != '':
                                        incident.extend(Incident.incident_comments,incident_comments).execute()
		
				incidents = iris_db.query(Incident)	
				#fix boxes not clearing
				return render_template("update_incident.html",
			                                title='Update Incident',
                        			        form=form,
			                                incidents=incidents)
	return render_template("update_incident.html",
                                title='Update Incident',
				form=form,
				incidents=incidents)


