import sys
sys.path.append('../')

from config.configApp import *
from services.user.index import *
userService = IndexUserServices()
from dtos.userdto import userDto

@api.route("/api/v1/user")
class User(Resource):
  def get(self):
    try:
      nickname = request.args.get('nickname')
      user = userService.showUser(nickname)
      return dumps(user)  
    except Exception as e:
      return dumps({'error': str(e)})

  def post(self):
    try:
      user = json.loads(request.data)
      saveduser = userService.userRegister(user)
      return dumps(saveduser)
    except Exception as e:
      return dumps({'error': str(e)})

@api.route("/api/v1/getallusers")
class GetAllUsers(Resource):
  def get(self):
    try:
      users = userService.showUsers()
      return dumps(users)
    except Exception as e:
      return dumps({'error': str(e)})

@api.route("/api/v1/updateuser")
class UpdateUser(Resource):
  def post(self):
    try:
      nickname = request.args.get('nickname')
      userdata = json.loads(request.data)
      user = userService.updateUser(nickname, userdata)
      return dumps(user)
    except Exception as e:
      return dumps({'error': str(e)})

@api.route("/api/v1/deleteuser")
class DeleteUser(Resource):
  def get(self):
    try:
      nickname = request.args.get('nickname')
      user = userService.removeUser(nickname)
      return dumps(user)
    except Exception as e:
      return dumps({'error': str(e)})