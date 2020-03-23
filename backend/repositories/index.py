import sys
sys.path.append("../")

from models.mongoSchemas.index import *
from repositories.userrepository import UserRepository
from repositories.roomrepository import RoomRepository
from dtos.userdto import userDto
from dtos.roomdto import room_dto

def indexRepositories() -> dict: 

  repositoriesDictionary = {
    'User': UserRepository(User, userDto),
    'Room': RoomRepository(Room, room_dto)
  }

  return repositoriesDictionary
