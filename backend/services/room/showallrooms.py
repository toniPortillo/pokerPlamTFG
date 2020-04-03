def show_all_rooms(room_repository, formatted_user_list, formatted_message_list) -> list:
    return [
        {
            'room_name': value['room_name'],
            'created_by': str(value['created_by']['id']),
            'room_date': value['room_date'],
            'users': formatted_user_list(value),
            'messages': formatted_message_list(value)
        }
        for value in room_repository.get_all()
    ]