class VoteRepository():
    def __init__(self, room_entity: dict, estimate_entity: dict, vote_entity: dict) -> None:
        self.room_entity = room_entity
        self.estimate_entity = estimate_entity
        self.vote_entity = vote_entity
    
    def create(self, room_name: str, estimateid: str ,vote_data: dict) -> dict:
        try:
            room  = self.room_entity
            vote  = self.vote_entity
            found_room = room.objects(room_name = room_name).first()
            saved_vote = vote(voteid = vote_data['voteid'], voter = vote_data['voter'],
            vote_content = vote_data['vote_content'])

            for value in found_room['estimates']:
                if(value['estimateid'] == estimateid):
                    value.votes.append(saved_vote)
                    found_room.save()
                    print(found_room['room_name'])
                    print(vote_data['voteid'])

                    return found_room
        except Exception:
            raise Exception('The vote was not created')