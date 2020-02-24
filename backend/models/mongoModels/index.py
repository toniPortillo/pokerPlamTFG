import sys
sys.path.append("../../")

from utils.connectMongo.database import *
from models.mongoModels.rawentity import rawEntity
db = mongodb()
rawModel = rawEntity(db)

def indexModels():
  modelDictionary = {
    'Raw' : rawModel['raw']
  }
  
  return modelDictionary