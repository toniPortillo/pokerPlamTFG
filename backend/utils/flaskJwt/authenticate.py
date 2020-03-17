import sys
sys.path.append('../../')

from repositories.index import *
repository = indexRepositories()
userRepository = repository['User']

def authenticate(username, password) -> dict:
    try:
        userexists = userRepository.findOneByNickname(username)
        correctpassword = check_password_hash(userexists['password'], password)
        if (userexists and correctpassword):
            return userexists
        else:
            raise Exception
    except Exception:
        raise Exception("User not exists or error password")
    