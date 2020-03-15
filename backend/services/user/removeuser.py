def removeUser(userRepository: object, nickname: str) -> int:
  userdeleted = userRepository.removeByNickname(nickname)

  return userdeleted