def add_user(room_repository: object, user_repository: object, room_name: str, nickname: str, check_user_in_room, room_dto: str, user_dto: dict) -> dict:
    try:
        found_room = room_repository.find_by_room_name(room_name)
        found_user = user_repository.findOneByNickname(nickname)
        user_is_in_the_room = check_user_in_room(found_room, nickname)
        if(found_room and found_user and user_is_in_the_room):
            updated_room = room_repository.add_user_to_list(found_room, found_user)
            
            if(updated_room == 1):
                room_dto['room_name'] = found_room['room_name']
                room_dto['created_by'] = str(found_room['created_by']['id'])
                room_dto['room_date'] = found_room['room_date']
                return room_dto
            else:
                message = "The user already exists in the room"
                return message
        else:
            message = "The user is in the room"
            return message
    except Exception:
        raise Exception("Room or user not found")