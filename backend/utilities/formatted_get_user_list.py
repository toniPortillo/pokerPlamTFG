def formatted_get_user_list(users: dict) -> dict:
    return [
        {
            'userid': value['userid'],
            'nickname': value['nickname'],
            'mail': value['mail']
        }
        for value in users
    ]