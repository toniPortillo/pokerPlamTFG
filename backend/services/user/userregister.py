def userRegister(userRepository: object, uuid: int, generate_password_hash: str, userData: dict, user_dto: dict) -> dict:
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

    user_created = userRepository.create(markeduser)
    user_dto['username'] = user_created['username']
    user_dto['nickname'] = user_created['nickname']
    user_dto['mail'] = user_created['mail']

    return user_dto