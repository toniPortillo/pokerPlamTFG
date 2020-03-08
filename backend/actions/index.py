import sys
sys.path.append('../')

from actions.useractions import *
from actions.checkmicroservice import *

checkMicroserviceAction = Hello()
userAction = User()
getAllUsersAction = GetAllUsers()
updateUserAction = UpdateUser()
deleteUserAction = DeleteUser()

