import sys
sys.path.append('../../')

from utils.connectMongoEngine.devdb import *

class User(db.Document):
  userid = db.StringField(required = True)
  username = db.StringField(required = True)
  nickname = db.StringField(required = True)
  password = db.StringField(required = True)
  mail = db.EmailField(required = True)