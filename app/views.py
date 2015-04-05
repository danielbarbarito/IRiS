from flask import render_template, redirect, url_for, request
from datetime import datetime
from app import app
from forms import NewAlertForm, UpdateAlertForm
from models import Alert, iris_db

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html",
				title='Home')


@app.route('/alert', methods=['GET', 'POST'])
def alert():

	alerts = iris_db.query(Alert)

	if request.method == 'POST':
		if request.form['btn'] == 'New':
			return redirect(url_for('new_alert'))
		elif request.form['btn'] == 'Update':
			selected = request.form.getlist('selected')
			return redirect(url_for('update_alert', selected=selected))
		elif request.form['btn'] == 'Promote':
			print 'promote'
	
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

