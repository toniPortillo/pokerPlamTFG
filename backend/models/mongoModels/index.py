import sys
sys.path.append("../../")

import os

from models.mongoSchemas.index import *
from models.mongoModels.userentity import userModel
from flask_mongoengine.wtf import model_form

def indexModels() -> dict:
  modelDictionary = {
    'User' : userModel(User)
  }
  
  return modelDictionary
