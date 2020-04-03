def formatted_user_list(room: dict) -> dict:
    return [
        {
            'username': value['username'],
            'nickname': value['nickname'],
            'mail': value['mail']
        }
        for value in room['users']
    ]