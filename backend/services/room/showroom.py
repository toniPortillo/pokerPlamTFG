def show_room(room_repository: object, room_name: str, room_dto: dict, formatted_user_list, formatted_message_list,
formatted_user_story_list, formatted_estimate_list, formatted_vote_list) -> dict:
    found_room = room_repository.find_by_room_name(room_name)
    
    room_dto['room_name'] = found_room['room_name']
    room_dto['created_by'] = str(found_room['created_by']['id'])
    room_dto['room_date'] = found_room['room_date']
    room_dto['users'] = formatted_user_list(found_room)
    room_dto['messages'] = formatted_message_list(found_room)
    room_dto['user_stories'] = formatted_user_story_list(found_room)
    room_dto['estimates'] = formatted_estimate_list(found_room, formatted_vote_list)

    return room_dto
    