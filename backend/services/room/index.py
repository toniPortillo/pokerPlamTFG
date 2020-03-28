import sys
sys.path.append('../../')
import datetime

from config.configFlaskJWTextended import *
from repositories.index import *
from dtos.roomdto import room_dto
#from utilities.list_formatter import list_formatter
from services.room.createroom import create_room
from services.room.showroom import show_room
from services.room.showallrooms import show_all_rooms

class IndexRoomServices():
    def __init__(self, repository: dict = indexRepositories(), room_dto: dict = room_dto) -> None:
        self.repository = repository['Room']
        self.user_repository = repository['User']
        self.room_dto = room_dto
    
    def create_room(self, room_data: dict, primary_user_key) -> dict:
        room  = create_room(self.repository, self.user_repository, room_data, primary_user_key, json, self.room_dto)

        return room

    def show_room(self, room_name: str) -> dict:
        room = show_room(self.repository, room_name, self.room_dto)

        return room

    def show_all_rooms(self) -> list:
        rooms = show_all_rooms(self.repository, self.room_dto)

        return rooms