def removeUser(userRepository: object, nickname: str, user_dto: dict) -> int:
    try:
        user_deleted = userRepository.removeByNickname(nickname)
        if (user_deleted == 1):
            user_dto['nickname'] = nickname

            return user_dto
        else:

            raise Exception
    except Exception:
        raise Exception("User not removed")