def create_room(room_repository: object, user_repository:object, room_data: dict, primary_user_key, json, room_dto: dict) -> dict:
    
    user_found = user_repository.find_by_mongo_id(primary_user_key)
    room_data['created_by'] = user_found['id']
    room_created = room_repository.create(room_data)

    room_dto['room_name'] = room_created['room_name']
    room_dto['created_by'] = str(room_created['created_by'])
    room_dto['room_date'] = room_created['room_date']
    room_dto['users'] = str(room_created['users'])
    room_dto['messages'] = [{}]

    return room_dto