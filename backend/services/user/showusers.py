def showUsers(userRepository: object, formatted_get_user_list) -> list:
  allUsers = userRepository.getAll()
  user_list = formatted_get_user_list(allUsers)

  return user_list