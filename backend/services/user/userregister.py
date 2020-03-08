def userRegister(userRepository, userData):
  user = userRepository
  userexists = user.findOneByNickname(userData['nickname'])
  
  usercreated = userRepository.create(userData)

  return usercreated