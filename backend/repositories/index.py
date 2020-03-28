import sys
sys.path.append("../")

from models.mongoSchemas.index import *
from repositories.userrepository import UserRepository
from repositories.roomrepository import RoomRepository
from dtos.roomdto import room_dto

def indexRepositories() -> dict: 

  repositoriesDictionary = {
    'User': UserRepository(User),
    'Room': RoomRepository(Room, room_dto)
  }

  return repositoriesDictionary