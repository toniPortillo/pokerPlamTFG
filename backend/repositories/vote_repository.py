class VoteRepository():
    def __init__(self, room_entity: dict, estimate_entity: dict, vote_entity: dict) -> None:
        self.room_entity = room_entity
        self.estimate_entity = estimate_entity
        self.vote_entity = vote_entity
    
    def create(self, room_name: str, estimateid: str, nickname: str, vote_data: dict) -> dict:
        try:
            room  = self.room_entity
            vote  = self.vote_entity
            found_room = room.objects(room_name = room_name).first()
            saved_vote = vote(voteid = vote_data['voteid'], voter = vote_data['voter'],
            vote_content = vote_data['vote_content'])

            for value in found_room['estimates']:
                if(value['estimateid'] == estimateid):
                    for vote in value['votes']:
                        if(vote['voter'] == nickname):
                            raise Exception("The user already voted")
                    value.votes.append(saved_vote)
                    found_room.save()

                    return found_room
        except Exception as e:
            raise Exception(str(e))

    def get_votes(self, room_name: str, estimateid: str) -> dict:
        try:
            room = self.room_entity
            found_room = room.objects(room_name = room_name).first()
            
            for value in found_room['estimates']:
                if(value['estimateid'] == estimateid):
                    if(len(value['votes']) == len(found_room['users'])):
                        return value
                    else:
                        raise Exception("Not all users voted")
        except Exception as e:
            raise Exception(str(e))

    def delete(self, room_name: str, estimateid: str, nickname: str) -> dict:
        try:
            room = self.room_entity
            found_room = room.objects(room_name = room_name).first()

            for value in found_room['estimates']:
                if(value['estimateid'] == estimateid):
                    for vote in value['votes']:
                        if(vote['voter'] == nickname):
                            value.votes.remove(vote)
                            found_room.save()
                            print(value['estimateid'])
                            return value
                    raise Exception("Your vote does not exist")
        except Exception as e:
            raise Exception(str(e))