import sys
sys.path.append('../../')

from repositories.index import *
repository = indexRepositories()
userRepository = repository['User']

def identity(payload):
    user_id = payload['identity']
    user = userRepository.findOneByUserId(user_id)

    return user