def userRegister(userRepository: object, generate_password_hash: str, userData: dict) -> dict:
  try:
    user = userRepository
    userexists = user.findOneByNickname(userData['nickname'])
    
    return("User already exists")
  except Exception:
    password = userData['password']
    userData['password'] = generate_password_hash(password)
    usercreated = userRepository.create(userData)
    
    return usercreated
