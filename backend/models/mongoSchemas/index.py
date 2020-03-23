import sys
sys.path.append('../../')
from utils.connectMongoEngine.database import *
import datetime
db = FactoryDatabase.get_database()

class User(db.Document):
    userid = db.StringField(required = True)
    username = db.StringField(required = True)
    nickname = db.StringField(required = True)
    password = db.StringField(required = True)
    mail = db.EmailField(required = True)

class Message(db.EmbeddedDocument):
    content = db.StringField(required = True)
    created_by = db.ReferenceField(User)
    message_date = db.DateTimeField(required = True)
    
class Room(db.Document):
    room_name = db.StringField(required = True)
    created_by = db.ReferenceField(User)
    room_date = db.DateTimeField(default=datetime.datetime.now())
    #users = db.ListField(db.ReferenceField(User))
    #messages = db.ListField(db.EmbeddedDocumentField(Message))
