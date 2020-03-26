def show_room(room_repository: object, room_name: str) -> dict:
    found_room = room_repository.find_by_room_name(room_name)

    return found_room
    