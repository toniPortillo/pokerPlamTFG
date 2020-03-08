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
    title='pokerPlam: Tool for the use of the Poker technique of planning by teams that work remotely.',
    description='pokerPlam apiRest', 
)
