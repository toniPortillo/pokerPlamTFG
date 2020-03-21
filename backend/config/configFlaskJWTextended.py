import os
import sys
sys.path.append('../')
import datetime

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, create_refresh_token,
    jwt_required, jwt_refresh_token_required, get_jwt_identity
)
from config.configApp import *

app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

jwt = JWTManager(app)