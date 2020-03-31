def create_message(message_repository: object, user_repository: object, message_data: dict, room_name: str, primary_user_key: str,
 message_dto: dict, room_dto: dict, user_dto: dict) -> dict:
    try:
        user_found = user_repository.find_by_mongo_id(primary_user_key)
        message_data['created_by'] = user_found['id']
        saved_message = message_repository.create(room_name, message_data)
    except Exception: