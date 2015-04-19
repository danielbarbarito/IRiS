WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
DEBUG = True
MONGO_DBNAME = 'iris_db'

#upload configs
#note: where shoule the folder be and what permissions should it have
UPLOAD_FOLDER = '/home/ramrod/IRiS/app/uploads'
ALLOWED_EXTENSIONS = set(['csv'])


#Alert/Incident Drop down configs
#ATYPE_CHOICES =
ASTATUS_CHOICES = [('',''),('Resolved','Resolved'),('Updated','Updated')] 
ITYPE_CHOICES = [('',''),('User','User'),('Policy','Policy'),('Network','Network')]
ISTATUS_CHOICES = [('',''),('Manual','Manual'),('Promoted','Promoted')]
