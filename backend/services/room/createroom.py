def create_room(room_repository: object, user_repository:object, room_data: dict, user_id, json) -> dict:
    
    user_found = user_repository.findOneByUserId(user_id)
    room_data['created_by'] = user_found[0]
    room_created = room_repository.create(room_data)
    print(room_created)
    return room_repository