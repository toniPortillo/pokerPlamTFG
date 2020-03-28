def updateUser(userRepository: object, nickname: str, userData: dict, user_dto: dict) -> dict:
    try:
        updated_user = userRepository.updateDataUser(nickname, userData)
        if (updated_user == 1):
            
            user_dto['username'] = userData['username']
            user_dto['nickname'] = nickname
            user_dto['mail'] = userData['mail']

            return user_dto
        else :
            raise Exception
    except Exception:
        raise Exception("Outdated user")