import sys
sys.path.append("../../")

from config.configMongoDB import *
config_mongodb = Config_MongoDB()

conf_db_dev = {
    'db': 'pokerPlamDEV',
    'host': config_mongodb.host,
    'port': config_mongodb.port
}