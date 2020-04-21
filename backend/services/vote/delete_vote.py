def delete_vote(vote_repository: object, room_name: str, estimateid: str, nickname: str, estimate_dto: dict,
formatted_vote_list) -> dict:
    try:
        updated_estimate = vote_repository.delete(room_name, estimateid, nickname)
        estimate_dto['estimateid'] = updated_estimate['estimateid']
        estimate_dto['title'] = updated_estimate['title']
        estimate_dto['final_value'] = updated_estimate['final_value']
        estimate_dto['commentary'] = updated_estimate['commentary']
        estimate_dto['created'] = str(updated_estimate['created_by']['id'])
        estimate_dto['votes'] = formatted_vote_list(updated_estimate)
        
        return estimate_dto
    except Exception as e:
        raise Exception(str(e))