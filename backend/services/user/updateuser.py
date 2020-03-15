def updateUser(userRepository: object, nickname: str, userData: dict) -> dict:
  updateduser = userRepository.updateDataUser(nickname, userData)

  return updateduser