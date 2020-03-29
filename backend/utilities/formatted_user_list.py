def formatted_user_list(user_repository: object, room: dict, user_dto: dict) -> dict:
    return [
        {
            'username': value['username'],
            'nickname': value['nickname'],
            'mail': value['mail']
        }
        for value in room['users']
    ]