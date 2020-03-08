def updateUser(userRepository, nickname, userData):
  updateduser = userRepository.updateDataUser(nickname, userData)

  return updateduser