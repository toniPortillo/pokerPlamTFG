def create_room(room_repository: object, user_repository:object, room_data: dict, primary_user_key, json) -> dict:
    
    user_found = user_repository.find_by_mongo_id(primary_user_key)
    room_data['created_by'] = user_found['id']
    room_created = room_repository.create(room_data)
    return room_created