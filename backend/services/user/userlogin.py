def userLogin(userRepository, check_password_hash, userData):
  try:
    user = userRepository
    userexists = user.findOneByNickname(userData['nickname'])
    correctpassword = check_password_hash(userexists['password'], userData['password'])
    if correctpassword:
      return("Here is the Token")
    else:
      raise Exception  
  except Exception:
    raise Exception("User not exists or error password")