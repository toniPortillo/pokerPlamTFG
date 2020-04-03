import sys
sys.path.append('../../')
import datetime

from config.configFlaskJWTextended import *
from repositories.index import *
from dtos.roomdto import room_dto
from dtos.userdto import userDto
from utilities.formatted_user_list import formatted_user_list
from utilities.formatted_message_list import formatted_message_list
from utilities.check_user_in_room import check_user_in_room
from utilities.check_creator import check_creator
from services.room.createroom import create_room
from services.room.showroom import show_room
from services.room.showallrooms import *
from services.room.add_user import add_user
from services.room.delete_user import delete_user
from services.room.delete_room import delete_room

class IndexRoomServices():
    def __init__(self, repository: dict = indexRepositories(), room_dto: dict = room_dto, user_dto: dict = userDto) -> None:
        self.repository = repository['Room']
        self.user_repository = repository['User']
        self.room_dto = room_dto
        self.user_dto = user_dto

    def create_room(self, room_data: dict, primary_user_key) -> dict:
        room  = create_room(self.repository, self.user_repository, room_data, primary_user_key, self.room_dto, formatted_user_list)

        return room

    def show_room(self, room_name: str) -> dict:
        room = show_room(self.repository, room_name, self.room_dto, formatted_user_list, formatted_message_list)

        return room

    def show_all_rooms(self) -> list:
        rooms = show_all_rooms(self.repository, formatted_user_list, formatted_message_list)

        return rooms

    def add_user(self, room_name: str, nickname: str) -> dict:
        room = add_user(self.repository, self.user_repository, room_name, nickname, check_user_in_room, self.room_dto, self.user_dto)

        return room

    def delete_user(self, room_name: str, nickname: str) -> dict:
        room = delete_user(self.repository, self.user_repository, room_name, nickname, check_user_in_room, check_creator, self.room_dto)

        return room

    def delete_room(self, room_name: str, nickname: str) -> dict:
        room = delete_room(self.repository, self.user_repository, room_name, nickname, check_creator)
        
        return room