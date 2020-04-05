import sys
sys.path.append('../')

from actions.checkmicroservice import *
from actions.useractions import *
from actions.roomactions import *
from actions.messageactions import *
from actions.user_story_actions import *

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
add_user_action = AddUser()
delete_user_action = DeleteUser()
delete_room_action = DeleteRoom()

# Check message actions
create_message_action = CreateMessage()
get_room_messages_action = ShowMessages()

# Check user story actions
create_user_story_action = CreateUserStory()
get_room_user_stories_action = ShowUserStories()
delete_user_story_action = DeleteUserStory()