def userLogin(userRepository: object, check_password_hash: str, userData: dict) -> str:
  try:
    user = userRepository
    userexists = user.findOneByNickname(userData['nickname'])
    correctpassword = check_password_hash(userexists['password'], userData['password'])
    if (userexists and correctpassword):
      return userexists
    else:
      raise Exception  
  except Exception:
    raise Exception("User not exists or error password")