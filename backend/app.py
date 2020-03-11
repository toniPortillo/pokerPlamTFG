import sys
sys.path.append("./")

from actions.index import *

# Actions / Endpoints

#check_microservice endpoint
checkMicroserviceAction

#user endpoint
loginAction
registerAction
showUserAction
getAllUsersAction
updateUserAction
deleteUserAction

if __name__ == '__main__':
  app.run('0.0.0.0', 5000, debug = True)


