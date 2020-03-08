import sys
sys.path.append("./")

from actions.index import *

# Actions / Endpoints

#check_microservice endpoint
checkMicroserviceAction

#user endpoint
userAction

if __name__ == '__main__':
  app.run('0.0.0.0', 5000, debug = True)


