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
show_all_rooms_action
add_user_action
delete_user_action
delete_room_action

# message endpoints
create_message_action
get_room_messages_action

# user story endpoints
create_user_story_action
get_room_user_stories_action
delete_user_story_action
modify_user_story_action

# estimate endpoints
create_estimate_action
delete_estimate_action
modify_final_value_action
modify_title_action
modify_commentary_action

if __name__ == '__main__':
  app.run('0.0.0.0', 5000, debug = True)


