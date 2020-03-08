def userRegister(userRepository, generate_password_hash, userData):
  try:
    user = userRepository
    userexists = user.findOneByNickname(userData['nickname'])
    print(userexists)
    
    return("User already exists")
  except Exception:
    password = userData['password']
    userData['password'] = generate_password_hash(password)
    usercreated = userRepository.create(userData)
    
    return usercreated
