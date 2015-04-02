from mongoalchemy.session import Session
from mongoalchemy.document import Document, Index
from mongoalchemy.fields import *

class Alert(Document):
	config_collection_name = 'alert'

	alert_name = StringField()
	alert_value = StringField()
	alert_status = StringField()
	alert_comments = StringField()

	def __str__(self):
		return '%s %s' % (self.alert_name, self.last_name)

iris_db = Session.connect('iris_db')

#will clear collection when python  run.py
#iris_db.clear_collection(Alert)
