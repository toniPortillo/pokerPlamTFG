import sys
sys.path.append("../")

from utils.connectMongo.database import *

client = mongodb();

def getcontact():
    return client.ContactDB
