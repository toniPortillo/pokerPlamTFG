import sys
sys.path.append('../')

import os
from flask_jwt import JWT, jwt_required, current_identity
from config.configApp import *
from utils.flaskJwt.authenticate import authenticate
from utils.flaskJwt.identity import identity

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

jwt = JWT(app, authenticate, identity)