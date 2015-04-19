from mongoalchemy.session import Session
from mongoalchemy.document import Document, Index
from mongoalchemy.fields import *


class Alert(Document):
	config_collection_name = 'alert'

	title = StringField()
	status = StringField()
	atype = ListField(AnythingField())
#	alert_generated = DateTimeField()
	entered = DateTimeField()
	ip = ListField(AnythingField())
        mac = ListField(AnythingField())
	comments = ListField(AnythingField())

	def __str__(self):
		return '%s %s %s' % (self.title, self.status,self.ip)


class Incident(Document):
	config_collection_name = 'incident'
	
	#incident_title = StringField()
	title = StringField()
	status = StringField()
	##idNum = StringField()
	itype = StringField()
	#itype = ListField(AnythingField())
	#incident_generated = DateTimeField()
	entered = DateTimeField()
	#incident_ip = ListField(AnythingField())
	#incident_mac = ListField(AnythingField())
	
	comments = ListField(AnythingField())
	
	alerts = ListField(RefField(type=DocumentField(Alert)))
	


iris_db = Session.connect('iris_db')

#will clear collection when python  run.py
#iris_db.clear_collection(Alert)
#iris_db.clear_collection(Incident)

