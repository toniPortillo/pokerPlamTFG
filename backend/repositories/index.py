import sys
sys.path.append("../")

from models.mongoSchemas.index import *
from repositories.userrepository import UserRepository
from dtos.userdto import userDto

def indexRepositories():

  repositoriesDictionary = {
    'User' : UserRepository(User, userDto)
  }

  return repositoriesDictionary
