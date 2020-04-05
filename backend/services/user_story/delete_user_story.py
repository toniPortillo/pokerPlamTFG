def delete_user_story(user_story_repository: object, storyid: str, room_name: str, room_dto: dict, formatted_user_list,
formatted_message_list, formatted_user_story_list) -> dict:
    try:
        updated_room = user_story_repository.delete_user_story(room_name, storyid)
        print(room_name)
        print(storyid)
        room_dto['room_name'] = updated_room['room_name']
        room_dto['created_by'] = str(updated_room['created_by']['id'])
        room_dto['users'] = formatted_user_list(updated_room)
        room_dto['messages'] = formatted_message_list(updated_room)
        room_dto['user_stories'] = formatted_user_story_list(updated_room)

        return room_dto 
    except Exception as e:
        raise Exception("User or room not found")