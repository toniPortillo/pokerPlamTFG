def userRegister(userRepository: object, uuid: int, generate_password_hash: str, userData: dict) -> dict:
  try:
    user = userRepository
    userexists = user.findOneByNickname(userData['nickname'])
    
    return("User already exists")
  except Exception:
    markeduser = {
      'userid': '',
      'username': '',
      'nickname': '',
      'password': '',
      'mail': ''
    }

    stringuuid = str(uuid)

    password = userData['password']
    markeduser['userid'] = stringuuid
    markeduser['username'] = userData['username']
    markeduser['nickname'] = userData['nickname']
    markeduser['password'] = generate_password_hash(password)
    markeduser['mail'] = userData['mail']

    usercreated = userRepository.create(markeduser)
    
    return usercreated