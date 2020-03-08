def showUser(userRepository, nickname):
  user = userRepository.findOneByNickname(nickname)

  return user