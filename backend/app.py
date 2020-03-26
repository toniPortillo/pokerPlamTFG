import sys
sys.path.append("./")

from actions.index import *

# Actions / Endpoints

# check_microservice endpoint
checkMicroserviceAction

# user endpoint
loginAction
registerAction
auth_user_action
showUserAction
getAllUsersAction
updateUserAction
deleteUserAction

# room endpoints
create_room_action
show_room_action
show_all_rooms

if __name__ == '__main__':
  app.run('0.0.0.0', 5000, debug = True)


