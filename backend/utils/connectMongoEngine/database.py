import sys
sys.path.append("../../")

import os
from flask_mongoengine import MongoEngine
from config.configApp import *
from utils.connectMongoEngine.devdb import *
from utils.connectMongoEngine.prodb import *
from utils.connectMongoEngine.testdb import *

db = MongoEngine()

class FactoryDatabase:
    @staticmethod
    def get_database(environment = os.environ['ENV']):
        if environment == "DEV":
            app.config['MONGODB_SETTINGS'] = conf_db_dev
            db.init_app(app)
            return db
        elif environment == "PRO":
            app.config['MONGODB_SETTINGS'] = conf_db_pro
            db.init_app(app)
            return db
        elif environment == "TEST":
            app.config['MONGODB_SETTINGS'] = conf_db_test
            db.init_app(app)
            return db
        else:
            app.config['MONGODB_SETTINGS'] = conf_db_test
            db.init_app(app)
            return db