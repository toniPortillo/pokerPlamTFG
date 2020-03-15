def showUsers(userRepository: object) -> list:
  allUsers = userRepository.getAll()

  return allUsers