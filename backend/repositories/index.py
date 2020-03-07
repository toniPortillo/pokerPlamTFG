import sys
sys.path.append("../")

from models.mongoSchemas.index import *
from repositories.userrepository import UserRepository

def indexRepositories():

  repositoriesDictionary = {
    'User' : UserRepository(User)
  }

  return repositoriesDictionary
