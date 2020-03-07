import sys
sys.path.append('../../')

from utils.connectMongoEngine.devdb import *

class User(db.Document):
  username = db.StringField(required = True)
  nickname = db.StringField(required = True)
  password = db.StringField(required = True)
  mail = db.EmailField(required = True)