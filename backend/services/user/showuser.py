def showUser(userRepository: object, nickname: str, user_dto) -> dict:
  user = userRepository.findOneByNickname(nickname)
  
  user_dto['username'] = user['username']
  user_dto['nickname'] = user['nickname']
  user_dto['mail'] = user['mail']

  return user_dto