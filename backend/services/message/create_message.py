def create_message(message_repository: object, user_repository: object, message_data: dict, room_name: str, primary_user_key: str,
message_dto: dict, room_dto: dict, user_dto: dict, formatted_user_list, formatted_message_list) -> dict:
    try:
        user_found = user_repository.find_by_mongo_id(primary_user_key)
        message_data['created_by'] = user_found['id']
        updated_room = message_repository.create(room_name, message_data)
        room_dto['room_name'] = updated_room['room_name']
        room_dto['created_by'] = str(updated_room['created_by']['id'])
        room_dto['room_date'] = updated_room['room_date']
        room_dto['users'] = formatted_user_list(user_repository, updated_room, user_dto)
        room_dto['messages'] = formatted_message_list(message_repository, updated_room, message_dto)

        return room_dto
    except Exception as e:
        raise Exception("User or room not found")