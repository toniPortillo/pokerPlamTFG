import sys
sys.path.append("../../")

import os
from mongoengine import connect
from config.configMongoDB import *
config_mongodb = Config_MongoDB()

class FactoryDatabase:
    @staticmethod
    def get_database(environment = os.environ['ENV']):
        if environment == "DEV":
            connect(
                'pokerPlamDBDEV',
                host = config_mongodb.host,
                port = config_mongodb.port
            )
        elif environment == "PRO":
            connect(
                'pokerPlamDBPRO',
                host = config_mongodb.host,
                port = config_mongodb.port
            )
        elif environment == "TEST":
            connect(
                'pokerPlamDBTEST',
                host = config_mongodb.host,
                port = config_mongodb.port
            )
        else:
            connect(
                'pokerPlamDBTEST',
                host = config_mongodb.host,
                port = config_mongodb.port
            )