def formatted_user_list(user_repository: object, room: dict, user_dto: dict) -> dict:
    user_list  = room['users']

    list_with_formatted_users = []

    for value in user_list:
        user_dto['username'] = value['username']
        user_dto['nickname'] = value['nickname']
        user_dto['mail'] = value['mail']

        list_with_formatted_users.append(user_dto)
    
    return list_with_formatted_users