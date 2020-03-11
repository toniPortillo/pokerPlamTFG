import os
from flask_jwt import JWT, jwt_required, current_identity
from configApp import app

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

jwt = JWT(app, authenticate, identity)