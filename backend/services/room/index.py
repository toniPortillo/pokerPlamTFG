import sys
sys.path.append('../../')
import datetime

from config.configFlaskJWTextended import *
from repositories.index import *
from services.room.createroom import create_room
from services.room.showroom import show_room
from services.room.showallrooms import show_all_rooms

class IndexRoomServices():
    def __init__(self, repository: dict = indexRepositories()) -> None:
        self.repository = repository['Room']
        self.user_repository = repository['User']
    
    def create_room(self, room_data: dict, user_id) -> dict:
        room  = create_room(self.repository, self.user_repository, room_data, user_id, json)

        return room

    def show_room(self, room_name: str) -> dict:
        room = show_room(self.repository, room_name)

        return room

    def show_all_rooms(self) -> list:
        rooms = show_all_rooms(self.repository)

        return rooms