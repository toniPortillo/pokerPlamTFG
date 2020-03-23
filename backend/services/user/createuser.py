def createUser(userRepository: object, userData: dict) -> dict:
    usercreated = userRepository.create(userData)

    return usercreated