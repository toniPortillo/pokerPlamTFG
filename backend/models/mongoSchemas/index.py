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
    message_date = DateTimeField(default = datetime.datetime.now())

class User_story(EmbeddedDocument):
    storyid = StringField(required = True)
    order_index = IntField(required = True)
    story_title = StringField(required = True)
    role = StringField(required = True)
    reason = StringField(required = True)
    estimate = IntField(required = True)
    importance = IntField(required = True)
    acceptance_criteria = StringField(required = True)
    created_by = ReferenceField(User)
    User_story_date = DateTimeField(default = datetime.datetime.now())

class Vote(EmbeddedDocument):
    voteid = StringField(required = True)
    voter = StringField(required = True)
    vote_content = StringField(required = True)
    vote_date = DateTimeField(default = datetime.datetime.now())

class Estimate(EmbeddedDocument):
    estimateid = StringField(required = True)
    title = StringField(required = True)
    final_value = IntField(required = True)
    commentary = StringField(required = True)
    created_by = ReferenceField(User)
    estimate_date = DateTimeField(default = datetime.datetime.now())
    votes = ListField(EmbeddedDocumentField(Vote))

class Room(Document):
    room_name = StringField(required = True)
    created_by = ReferenceField(User)
    room_date = DateTimeField(default = datetime.datetime.now())
    users = ListField(ReferenceField(User))
    messages = ListField(EmbeddedDocumentField(Message))
    user_stories = ListField(EmbeddedDocumentField(User_story))
    estimates = ListField(EmbeddedDocumentField(Estimate))
