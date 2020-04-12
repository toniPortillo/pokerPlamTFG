def formatted_vote_list(estimate: dict) -> list:
    return [
        {
            'voteid': value['voteid'],
            'voter': value['voter'],
            'vote_content': value['vote_content']
        }
        for value in estimate['votes']
    ]