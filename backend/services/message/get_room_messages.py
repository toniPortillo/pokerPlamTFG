def get_room_messages(room_repository: object, room_name: str, formatted_message_list) -> list:
    try:
        found_room = room_repository.find_by_room_name(room_name)

        message_list = formatted_message_list(found_room)
        return message_list
    except Exception:
        raise Exception("The room does not exist")