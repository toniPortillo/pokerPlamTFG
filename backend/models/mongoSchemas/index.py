import sys
sys.path.append('../../')

import datetime
from mongoengine import *
from utils.mongoengine.database import *
FactoryDatabase.get_database()

class User(Document):
    userid = StringField(required = True)
    username = StringField(required = True)
    nickname = StringField(required = True)
    password = StringField(required = True)
    mail = EmailField(required = True)

class Message(EmbeddedDocument):
    order_index = IntField(required = True)
    content = StringField(required = True)
    created_by = ReferenceField(User)
    message_date = DateTimeField(default=datetime.datetime.now())
    
class Room(Document):
    room_name = StringField(required = True)
    created_by = ReferenceField(User)
    room_date = DateTimeField(default=datetime.datetime.now())
    users = ListField(ReferenceField(User))
    messages = ListField(EmbeddedDocumentField(Message))
