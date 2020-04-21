import sys
sys.path.append('../../')
import uuid

from config.configFlaskJWTextended import *
from repositories.index import *
from dtos.message_dto import message_dto
from dtos.roomdto import room_dto
from dtos.userdto import userDto
from utilities.formatted_message_list import formatted_message_list
from utilities.formatted_user_list import formatted_user_list
from utilities.formatted_user_story_list import formatted_user_story_list
from utilities.formatted_estimate_list import formatted_estimate_list
from utilities.formatted_vote_list import formatted_vote_list
from services.user_story.create_user_story import create_user_story
from services.user_story.get_room_user_stories import get_room_user_stories
from services.user_story.delete_user_story import delete_user_story
from services.user_story.modify_user_story import modify_user_story

class IndexUserStoryServices():
    def __init__(self, repository: dict = indexRepositories(), room_dto: dict = room_dto, user_dto: dict = userDto) -> None:
        self.repository = repository['User_story']
        self.user_repository = repository['User']
        self.room_repository = repository['Room']
        self.room_dto = room_dto
        self.user_dto = user_dto

    def create_user_story(self, user_story_data: dict, room_name: str, primary_user_key: str) -> dict:
        storyid = uuid.uuid4()

        user_story = create_user_story(self.repository, self.user_repository, storyid, user_story_data, room_name, primary_user_key,
        self.room_dto, formatted_user_list, formatted_message_list, formatted_user_story_list, formatted_estimate_list, 
        formatted_vote_list)

        return user_story

    def get_room_user_stories(self, room_name: str) -> list:
        user_story_list = get_room_user_stories(self.room_repository, room_name, formatted_user_story_list)

        return user_story_list

    def delete_user_story(self, room_name: str, storyid: str) -> dict:
        user_story = delete_user_story(self.repository, storyid, room_name, room_dto, formatted_user_list, formatted_message_list, 
        formatted_user_story_list, formatted_estimate_list, formatted_vote_list)

        return user_story

    def modify_user_story(self, storyid: str, user_story_data: dict) -> dict:
        user_story = modify_user_story(self.repository, storyid, user_story_data, room_dto, formatted_user_list,
        formatted_message_list, formatted_user_story_list, formatted_estimate_list, formatted_vote_list)

        return user_story