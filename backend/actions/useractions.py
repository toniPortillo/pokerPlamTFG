import sys
sys.path.append('../')

from config.configApp import *
from services.user.index import *
userService = IndexUserServices()

@api.route("/api/v1/user")
class User(Resource):
  def get(self):
    try:
      users = userService.showUser()
      return dumps(users)
    except Exception as e:
      return dumps({'error': str(e)})

  def post(self):
    try:
      user = json.loads(request.data)
      status = userService.createUser(user)
      return dumps({'message': 'SUCCESS'})
    except Exception as e:
      return dumps({'error': str(e)})