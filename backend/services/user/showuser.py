def showUser(userRepository: object, nickname: str) -> dict:
  user = userRepository.findOneByNickname(nickname)

  return user