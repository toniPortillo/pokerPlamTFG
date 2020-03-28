def auth_user(userRepository: object, check_password_hash: str, create_access_token, create_refresh_token, user_data: dict, user_dto: dict) -> dict:
    try:
        user = userRepository
        user_exists = user.findOneByNickname(user_data['nickname'])
        correct_password = check_password_hash(user_exists['password'], user_data['password'])
        
        if (user_exists and correct_password):
            access_token = create_access_token(identity = user_data)
            refresh_token = create_refresh_token(identity = user_data)
            user_dto['pk'] = str(user_exists['id'])
            user_dto['id'] = user_exists['userid']
            user_dto['username'] = user_exists['username']
            user_dto['nickname'] = user_exists['nickname']
            user_dto['mail'] = user_exists['mail']
            user_dto['token'] = access_token
            user_dto['refresh'] = refresh_token
            
            return user_dto
        else:
            raise Exception
    except Exception:
        raise Exception("User not exists or error password")