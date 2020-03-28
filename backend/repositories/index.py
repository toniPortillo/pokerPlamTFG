import sys
sys.path.append("../")

from models.mongoSchemas.index import *
from repositories.userrepository import UserRepository
from repositories.roomrepository import RoomRepository

def indexRepositories() -> dict: 

  repositoriesDictionary = {
    'User': UserRepository(User),
    'Room': RoomRepository(Room)
  }

  return repositoriesDictionary