import sys
sys.path.append('../../')

from config.configFlaskJWTextended import *
from repositories.index import *
from dtos.message_dto import message_dto
from dtos.roomdto import room_dto
from dtos.userdto import userDto
from utilities.formatted_user_list import formatted_user_list
from utilities.formatted_message_list import formatted_message_list
from services.message.create_message import create_message

class IndexMessageServices():
    def __init__(self, repository: dict = indexRepositories(), message_dto = message_dto, room_dto = room_dto, user_dto = userDto) -> None:
        self.repository = repository['Message']
        self.user_repository = repository['User']
        self.room_repository = repository['Room']
        self.message_dto = message_dto
        self.room_dto = room_dto
        self.user_dto = user_dto

    def create_message(self, message_data: dict, room_name: str, primary_user_key: str) -> dict:
        message = create_message(self.repository, self.user_repository, message_data, room_name, primary_user_key, self.message_dto,
        self.room_dto, self.user_dto, formatted_user_list, formatted_message_list)

        return message