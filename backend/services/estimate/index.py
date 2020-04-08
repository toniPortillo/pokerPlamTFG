import sys
sys.path.append('../../')
import uuid

from config.configFlaskJWTextended import *
from repositories.index import *
from dtos.roomdto import room_dto
from utilities.formatted_message_list import formatted_message_list
from utilities.formatted_user_list import formatted_user_list
from utilities.formatted_user_story_list import formatted_user_story_list
from utilities.formatted_estimate_list import formatted_estimate_list
from services.estimate.create_estimate import create_estimate

class IndexEstimateServices():
    def __init__(self, repository: dict = indexRepositories(), room_dto: dict = room_dto) -> None:
        self.repository = repository['Estimate']
        self.user_repository = repository['User']
        self.room_repository = repository['Room']
        self.room_dto = room_dto

    def create_estimate(self, estimate_date: dict, room_name: str, primary_user_key: str) -> dict:
        estimateid = uuid.uuid4()

        estimate = create_estimate(self.repository, self.user_repository, estimateid, estimate_date, room_name, primary_user_key,
        self.room_dto, formatted_user_list, formatted_message_list, formatted_user_story_list, formatted_estimate_list)

        return estimate