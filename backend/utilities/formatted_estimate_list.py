def formatted_estimate_list(room: dict, formatted_vote_list) -> list:
    return [
        {
            'estimateid': value['estimateid'],
            'title': value['title'],
            'final_value': value['final_value'],
            'commentary': value['commentary'],
            'created_by': str(value['created_by']['id']),
            'votes': formatted_vote_list(value)
        }
        for value in room['estimates']
    ]