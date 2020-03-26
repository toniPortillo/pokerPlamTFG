import sys
sys.path.append('../')

from actions.checkmicroservice import *
from actions.useractions import *
from actions.roomactions import *
# Check microservice action
checkMicroserviceAction = Hello()

# Check user actions
loginAction = Login()
registerAction = Register()
auth_user_action = AuthUser()
showUserAction = GetUser()
getAllUsersAction = GetAllUsers()
updateUserAction = UpdateUser()
deleteUserAction = DeleteUser()

# Check room actions
create_room_action = CreateRoom()
show_room_action = ShowRoom()
show_all_rooms_action = ShowAllRooms()