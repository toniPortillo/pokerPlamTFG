def createUser(userRepository, userData):
  usercreated = userRepository.create(userData)

  return usercreated