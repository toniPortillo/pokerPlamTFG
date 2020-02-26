import sys
sys.path.append("../../")

import os
from utils.connectMongo.database import *
from models.mongoModels.rawentity import rawEntity

db = FactoryDatabase.get_database(os.environ["ENV"])
rawModel = rawEntity(db)

def indexModels():
  modelDictionary = {
    'Raw' : rawModel['raw']
  }
  
  return modelDictionary
