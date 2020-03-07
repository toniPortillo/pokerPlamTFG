import sys
sys.path.append("../../")

from flask_mongoengine import MongoEngine

from config.configApp import *

db = MongoEngine()

app.config['MONGODB_SETTINGS'] = {
  'db': 'pokerPlamDev',
  'host': 'localhost',
  'port': 27017
}

db.init_app(app)