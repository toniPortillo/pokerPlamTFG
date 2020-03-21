import sys
sys.path.append('../')

from actions.useractions import *
from actions.checkmicroservice import *

checkMicroserviceAction = Hello()
loginAction = Login()
registerAction = Register()
auth_user_action = AuthUser()
showUserAction = GetUser()
getAllUsersAction = GetAllUsers()
updateUserAction = UpdateUser()
deleteUserAction = DeleteUser()