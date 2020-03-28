def show_room(room_repository: object, user_repository: object, room_name: str, room_dto: dict, user_dto: dict, formatted_user_list) -> dict:
    found_room = room_repository.find_by_room_name(room_name)
    
    room_dto['room_name'] = found_room['room_name']
    room_dto['created_by'] = str(found_room['created_by']['id'])
    room_dto['room_date'] = found_room['room_date']
    room_dto['users'] = formatted_user_list(user_repository, found_room, user_dto)
    room_dto['messages'] = [{}]

    return room_dto
    