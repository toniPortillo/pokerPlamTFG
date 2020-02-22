import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
import sys
sys.path.append("./")

from models.contact import *
from flask import Flask
from flask import request
from flask_restplus import Api, Resource
from bson.json_util import dumps
import json
import os

modelContact = getcontact()

app = Flask(__name__)
api = Api(app, version='1.0', 
    title='Prueba concepto UnitTest Flask MongoDB',
    description='Microservice oriented to Open Items operations.', 
)

@api.route("/api/v1/hello")
class Hello(Resource):
    def get(self):
        return "Welcome to Python Flask!"

@api.route("/api/v1/add_contact")
class Add(Resource):
    def post(self):
        try:
            data = json.loads(request.data)
            status = modelContact.Contacts.insert_one(
                data
            )
            return dumps({'message': 'SUCCESS'})
        except Exception as e:
            return dumps({'error': str(e)})

@api.route("/api/v1/get_all_contact")
class Get_all(Resource):
    def get(self):
        try:
            contacts = modelContact.Contacts.find()
            return dumps(contacts)
        except Exception as e:
            return dumps({'error': str(e)})

if __name__ == '__main__':
  app.run('0.0.0.0', 5000, debug = True)
