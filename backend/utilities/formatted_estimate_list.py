def formatted_estimate_list(room: dict) -> list:
    return [
        {
            'estimateid': value['estimateid'],
            'title': value['title'],
            'final_value': value['final_value'],
            'commentary': value['commentary'],
            'created_by': str(value['created_by']['id'])
        }
        for value in room['estimates']
    ]