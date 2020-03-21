import sys
sys.path.append('../')

from config.configApp import *
from services.user.index import *
userService = IndexUserServices()
from dtos.userdto import userDto

@api.route("/api/v1/login")
class Login(Resource):
  def post(self) -> dict:
    try:
      user = json.loads(request.data)
      loggeduser = userService.userLogin(user)
      return dumps(loggeduser)
    except Exception as e:
      return dumps({'error': str(e)})

@api.route("/api/v1/register")
class Register(Resource):
  def post(self) -> dict:
    try:
      user = json.loads(request.data)
      saveduser = userService.userRegister(user)
      return dumps(saveduser)
    except Exception as e:
      return dumps({'error': str(e)})

@api.route("/api/v1/auth")
class AuthUser(Resource):
  def post(self) -> dict:
    try:
      user = json.loads(request.data)
      saveduser = userService.auth_user(user)
      return dumps(saveduser)
    except Exception as e:
      return dumps({'error': str(e)})

@api.route('/api/v1/showuser')
class GetUser(Resource):
  @jwt_required
  def get(self) -> dict:
    try:
      nickname = request.args.get('nickname')
      user = userService.showUser(nickname)
      return dumps(user)  
    except Exception as e:
      return dumps({'error': str(e)})


@api.route("/api/v1/getallusers")
class GetAllUsers(Resource):
  def get(self) -> list:
    try:
      users = userService.showUsers()
      return dumps(users)
    except Exception as e:
      return dumps({'error': str(e)})

@api.route("/api/v1/updateuser")
class UpdateUser(Resource):
  def post(self) -> dict:
    try:
      nickname = request.args.get('nickname')
      userdata = json.loads(request.data)
      user = userService.updateUser(nickname, userdata)
      return dumps(user)
    except Exception as e:
      return dumps({'error': str(e)})

@api.route("/api/v1/deleteuser")
class DeleteUser(Resource):
  def get(self) -> dict:
    try:
      nickname = request.args.get('nickname')
      user = userService.removeUser(nickname)
      return dumps(user)
    except Exception as e:
      return dumps({'error': str(e)})