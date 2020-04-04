import sys
sys.path.append("../")

from models.mongoSchemas.index import *
from repositories.userrepository import UserRepository
from repositories.roomrepository import RoomRepository
from repositories.message_repository import MessageRepository
from repositories.user_story_repository import UserStoryRepository

def indexRepositories() -> dict: 

  repositoriesDictionary = {
    'User': UserRepository(User),
    'Room': RoomRepository(Room),
    'Message': MessageRepository(Room, Message),
    'User_story': UserStoryRepository(Room, User_story)
  }

  return repositoriesDictionary