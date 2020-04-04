def formatted_user_story_list(room: dict) -> list:
    return [
        {
            'order_index': value['order_index'],
            'story_title': value['story_title'],
            'role': value['role'],
            'reason': value['reason'],
            'estimate': value['estimate'],
            'importance': value['importance'],
            'acceptance_criteria': value['acceptance_criteria'],
            'created_by': str(value['created_by']['id'])
        }
        for value in room['user_stories']
    ]