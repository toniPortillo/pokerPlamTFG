import sys
sys.path.append("../../")

import os

from config.developmentMongoDB import Development_MongoDB
from pymongo import MongoClient

environmentDatabase = Development_MongoDB()

def mongodb():
    client = MongoClient(environmentDatabase.gethost(), environmentDatabase.getport())
    return client.PocDB
