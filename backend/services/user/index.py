import sys
sys.path.append('../../')
import uuid

from config.configFlaskJWTextended import *
from werkzeug.security import generate_password_hash, check_password_hash
from repositories.index import *
from services.user.createuser import createUser
from services.user.userregister import userRegister
from services.user.userlogin import userLogin
from services.user.authuser import auth_user
from services.user.showuser import showUser
from services.user.removeuser import removeUser
from services.user.showusers import showUsers
from services.user.updateuser import updateUser

class IndexUserServices():
    def __init__(self, repository: dict = indexRepositories()) -> None:
        self.repository = repository['User']

    def createUser(self, userData: dict) -> dict:
        user = createUser(self.repository, userData)

        return user

    def userRegister(self, userData: dict) -> dict:
        uid = uuid.uuid4()
        user = userRegister(self.repository, uid, generate_password_hash, userData)
    
        return user

    def userLogin(self, userData: dict) -> dict:
        user = userLogin(self.repository, check_password_hash, userData)

        return user

    def auth_user(self, userData: dict) -> dict:
        user = auth_user(self.repository, check_password_hash, create_access_token, create_refresh_token, userData)

        return user

    def showUser(self, nickname: str) -> dict:
        user = showUser(self.repository, nickname)

        return user

    def showUsers(self) -> list:
        users = showUsers(self.repository)

        return users

    def updateUser(self, nickname: str, userData: dict) -> int:
        user = updateUser(self.repository, nickname, userData)

        return user

    def removeUser(self, nickname: str) -> int:
        user = removeUser(self.repository, nickname)

        return user