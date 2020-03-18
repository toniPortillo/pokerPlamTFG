import sys
sys.path.append('../')

import os
from flask_jwt import JWT, jwt_required, current_identity
from config.configApp import *
from utils.flaskJwt.authenticate import *
from utils.flaskJwt.identity import *

app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)