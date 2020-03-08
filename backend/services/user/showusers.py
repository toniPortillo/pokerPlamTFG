def showUsers(userRepository):
  allUsers = userRepository.getAll()

  return allUsers