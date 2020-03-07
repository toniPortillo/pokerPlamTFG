import sys
sys.path.append('../../')

from repositories.index import *
from services.user.createuser import createUser
from services.user.showuser import showUser

class IndexUserServices():
  def __init__(self, repository = indexRepositories()):
    self.repository = repository['User']

  def createUser(self, userData):
    user = createUser(self.repository, userData)

    return user

  def showUser(self):
    users = showUser(self.repository)

    return users    