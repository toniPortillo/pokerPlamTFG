def show_all_rooms(room_repository, formatted_user_list, formatted_message_list, formatted_user_story_list, 
formatted_estimate_list, formatted_vote_list) -> list:
    return [
        {
            'room_name': value['room_name'],
            'created_by': str(value['created_by']['id']),
            'room_date': value['room_date'],
            'users': formatted_user_list(value),
            'messages': formatted_message_list(value),
            'user_stories': formatted_user_story_list(value),
            'estimates': formatted_estimate_list(value, formatted_vote_list)
        }
        for value in room_repository.get_all()
    ]