def userLogin(userRepository, check_password_hash, nickname, password):
  try:
    user = userRepository
    userexists = user.findOneByNickname(nickname)
    correctpassword = check_password_hash(userexists['password'], password)
    if correctpassword:
      return("Here is the Token")
    else:
      raise Exception  
  except Exception:
    raise Exception("User not exists or error password")