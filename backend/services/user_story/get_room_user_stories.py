def get_room_user_stories(room_repository: object, room_name: str, formatted_user_story_list) -> list:
    try:
        found_room = room_repository.find_by_room_name(room_name)

        user_story_list = formatted_user_story_list(found_room)
        return user_story_list
    except Exception:
        raise Exception("The room does not exist")