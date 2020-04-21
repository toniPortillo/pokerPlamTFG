import sys
sys.path.append('../../')
import uuid

from config.configFlaskJWTextended import *
from repositories.index import *
from dtos.roomdto import room_dto
from dtos.estimate_dto import estimate_dto
from utilities.formatted_user_list import formatted_user_list
from utilities.formatted_message_list import formatted_message_list
from utilities.formatted_user_story_list import formatted_user_story_list
from utilities.formatted_estimate_list import formatted_estimate_list
from utilities.formatted_vote_list import formatted_vote_list
from services.vote.create_vote import create_vote
from services.vote.show_votes import show_votes
from services.vote.delete_vote import delete_vote

class IndexVoteServices():
    def __init__(self, repository: dict = indexRepositories(), room_dto: dict = room_dto) -> None:
        self.repository = repository['Vote']
        self.room_repository = repository['Room']
        self.room_dto = room_dto
        self.estimate_dto = estimate_dto

    def create_vote(self, vote_data: dict, room_name: str, estimateid: str, nickname: str) -> dict:
        voteid = uuid.uuid4()

        vote = create_vote(self.repository, estimateid, nickname, voteid, vote_data, room_name, self.room_dto, 
        formatted_user_list, formatted_message_list, formatted_user_story_list, formatted_estimate_list, 
        formatted_vote_list)

        return vote

    def show_votes(self, room_name: str, estimateid: str) -> dict:
        estimate = show_votes(self.repository, room_name, estimateid, self.estimate_dto, formatted_vote_list)

        return estimate

    def delete_vote(self, room_name: str, estimateid: str, nickname: str) -> dict:
        estimate =  delete_vote(self.repository, room_name, estimateid, nickname, self.estimate_dto, formatted_vote_list)

        return estimate