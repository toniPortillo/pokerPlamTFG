import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask
from flask import request
from flask_restplus import Api, Resource
import json
from bson.json_util import dumps
import os

app = Flask(__name__)
api = Api(app, version='1.0', 
    title='Prueba concepto UnitTest Flask MongoDB',
    description='Microservice oriented to Open Items operations.', 
)
