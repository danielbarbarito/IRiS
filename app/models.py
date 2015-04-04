from mongoalchemy.session import Session
from mongoalchemy.document import Document, Index
from mongoalchemy.fields import *


class Alert(Document):
	config_collection_name = 'alert'

	alert_title = StringField()
	alert_status = StringField()
	alert_type = ListField(AnythingField())
#	alert_generated = DateTimeField()
	alert_entered = DateTimeField()
	alert_ip = ListField(AnythingField())
        alert_mac = ListField(AnythingField())
	alert_comments = ListField(AnythingField())

	def __str__(self):
		return '%s %s %s' % (self.alert_title, self.alert_status,self.alert_ip)


class Incident(Document):
	config_collection_name = 'incident'
	
	incident_title = StringField()
	incident_status = StringField()
	incident_type = ListField(AnythingField())
	#incident_generated = DateTimeField()
	incident_entered = DateTimeField()
	incident_ip = ListField(AnythingField())
	incident_mac = ListField(AnythingField())
	incident_comments = ListField(AnythingField())

	

iris_db = Session.connect('iris_db')

#will clear collection when python  run.py
#iris_db.clear_collection(Alert)
#iris_db.clear_collection(Incident)
