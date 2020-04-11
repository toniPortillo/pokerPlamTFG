def modify_commentary(estimate_repository: object, estimateid: str, commentary: str, room_dto: dict,
formatted_user_list, formatted_message_list, formatted_user_story_list, formatted_estimate_list) -> dict:
    try:
        updated_room = estimate_repository.modify_commentary(estimateid, commentary)
        room_dto['room_name'] = updated_room['room_name']
        room_dto['created_by'] = str(updated_room['created_by']['id'])
        room_dto['users'] = formatted_user_list(updated_room)
        room_dto['messages'] = formatted_message_list(updated_room)
        room_dto['user_stories'] = formatted_user_story_list(updated_room)
        room_dto['estimates'] = formatted_estimate_list(updated_room)

        return room_dto
    except Exception:
        raise Exception("Estimate not found")