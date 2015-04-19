from flask import Flask
from flask.ext.pymongo import PyMongo

#until config works
#UPLOAD_FOLDER = '/home/ramrod/IRiS/app/uploads'
#ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config.from_object('config')
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import views
