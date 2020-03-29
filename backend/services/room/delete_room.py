def delete_room(room_repository: object, user_repository: object, room_name: str, nickname: str, check_creator) -> str:
    try:
        found_room = room_repository.find_by_room_name(room_name)
        found_user = user_repository.findOneByNickname(nickname)
        creator_user = check_creator(found_room, found_user)
        if(found_room and found_user and not creator_user):
            removed_room = room_repository.delete(room_name)
            print("Estoy aqui")
            if(removed_room == 1):
                message = "Room successfully removed"
                return message
            else:
                message = "The room could not be deleted"
                return message
        else:
            message = "The room does not exist or the user is not the creator"
            return message
    except Exception:
        raise Exception("Room or user not found")