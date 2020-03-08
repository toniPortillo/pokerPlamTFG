def updateUser(userRepository, nickname, userData):
  updateduser = userRepository.update(nickname, userData)

  return updateduser