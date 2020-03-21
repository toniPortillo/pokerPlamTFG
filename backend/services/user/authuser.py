def auth_user(userRepository: object, check_password_hash: str, create_access_token, create_refresh_token, user_data: dict) -> dict:
    try:
        user = userRepository
        user_exists = user.findOneByNickname(user_data['nickname'])
        correct_password = check_password_hash(user_exists['password'], user_data['password'])
        if (user_exists and correct_password):
            del user_exists['password']
            access_token = create_access_token(identity = user_data)
            refresh_token = create_refresh_token(identity = user_data)
            user_exists['token'] = access_token
            user_exists['refresh'] = refresh_token
            return user_exists
        else:
            raise Exception
    except Exception:
        raise Exception("User not exists or error password")