def show_room(room_repository: object, room_name: str, room_dto: dict) -> dict:
    found_room = room_repository.find_by_room_name(room_name)
    
    room_dto['room_name'] = found_room['room_name']
    room_dto['created_by'] = str(found_room['created_by']['id'])
    room_dto['room_date'] = found_room['room_date']
    room_dto['users'] = str(found_room['users'][0]['id'])
    room_dto['messages'] = {}

    return room_dto
    