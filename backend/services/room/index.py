import sys
sys.path.append('../../')
import datetime

from config.configFlaskJWTextended import *
from repositories.index import *
from services.room.createroom import create_room

class IndexRoomServices():
    def __init__(self, repository: dict = indexRepositories()) -> None:
        self.repository = repository['Room']
        self.user_repository = repository['User']
    
    def create_room(self, room_data: dict, user_id) -> dict:
        room  = create_room(self.repository, self.user_repository, room_data, user_id, json)

        return room