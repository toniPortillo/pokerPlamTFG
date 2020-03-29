def show_all_rooms(room_repository, user_repository, user_dto, formatted_user_list):
    return [
        {
            'room_name': value['room_name'],
            'created_by': str(value['created_by']['id']),
            'room_date': value['room_date'],
            'users': formatted_user_list(user_repository, value, user_dto)
        }
        for value in room_repository.get_all()
    ]