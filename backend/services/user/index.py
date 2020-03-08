import sys
sys.path.append('../../')

from werkzeug.security import generate_password_hash, check_password_hash
from repositories.index import *
from services.user.createuser import createUser
from services.user.userregister import userRegister
from services.user.showuser import showUser
from services.user.removeuser import removeUser
from services.user.showusers import showUsers
from services.user.updateuser import updateUser

class IndexUserServices():
  def __init__(self, repository = indexRepositories()):
    self.repository = repository['User']

  def createUser(self, userData):
    user = createUser(self.repository, userData)

    return user

  def userRegister(self, userData):
    user = userRegister(self.repository, generate_password_hash, userData)
    
    return user

  def showUser(self, nickname):
    user = showUser(self.repository, nickname)

    return user

  def showUsers(self):
    users = showUsers(self.repository)

    return users

  def updateUser(self, nickname, userData):
    user = updateUser(self.repository, nickname, userData)

    return user

  def removeUser(self, nickname):
    user = removeUser(self.repository, nickname)

    return user