import sys
sys.path.append("../../")

import os

from config.developmentMongoDB import Development_MongoDB
from pymongo import MongoClient

developmentDB = Development_MongoDB()

def mongodb():
    client = MongoClient()
    return client
