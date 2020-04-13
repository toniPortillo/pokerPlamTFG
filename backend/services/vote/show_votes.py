def show_votes(vote_repository: object, room_name: str, estimateid: str, estimate_dto: dict, 
formatted_vote_list) -> dict:
    try:
        get_estimate = vote_repository.get_votes(room_name, estimateid)
        estimate_dto['estimateid'] = get_estimate['estimateid']
        estimate_dto['title'] = get_estimate['title']
        estimate_dto['final_value'] = get_estimate['final_value']
        estimate_dto['commentary'] = get_estimate['commentary']
        estimate_dto['created'] = str(get_estimate['created_by']['id'])
        estimate_dto['votes'] = formatted_vote_list(get_estimate)

        return estimate_dto
    except Exception as e:
        raise Exception(str(e))