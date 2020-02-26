import sys
sys.path.append("../")

from models.mongoModels.index import *
from repositories.rawrepository import *

rawEntity = indexModels()

def indexRepositories():

  repositoriesDictionary = {
    'Raw' : RawRepository(rawEntity['Raw'])
  }

  return repositoriesDictionary
