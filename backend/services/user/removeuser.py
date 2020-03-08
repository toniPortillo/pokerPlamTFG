def removeUser(userRepository, nickname):
  userdeleted = userRepository.removeByNickname(nickname)

  return userdeleted