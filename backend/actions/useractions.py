import sys
sys.path.append('../')

from services.user.index import *
userService = IndexUserServices()

from config.configFlaskJWTextended import *
from utils.flaskJWTextend.unauthorized_loader import *

@api.route("/api/v1/login")
class Login(Resource):
    def post(self) -> dict:
        try:
            user = json.loads(request.data)
            logged_user = userService.userLogin(user)
            response = jsonify(ok = True, data = logged_user)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response

@api.route("/api/v1/register")
class Register(Resource):
    def post(self) -> dict:
        try:
            user = json.loads(request.data)
            saved_user = userService.userRegister(user)
            response = jsonify(ok = True, data = saved_user)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response

@api.route("/api/v1/auth")
class AuthUser(Resource):
    def post(self) -> dict:
        try:
            user = json.loads(request.data)
            authorized_user = userService.auth_user(user)
            response = jsonify(ok = True, data = authorized_user)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response

@api.route("/api/v1/refresh")
class RefreshToken(Resource):
    @jwt_refresh_token_required
    def post(self) -> dict:
        current_user = get_jwt_identity()
        ret = {
            'token': create_access_token(identity = current_user)
        }
        response = jsonify(
            ok = True,
            data = ret
        )
        response.status_code = 200
        return response

@api.route('/api/v1/showuser')
class GetUser(Resource):
    @jwt_required
    def get(self) -> dict:
        try:
            nickname = request.args.get('nickname')
            user = userService.showUser(nickname)
            response = jsonify(ok = True, data = user)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response

@api.route("/api/v1/getallusers")
class GetAllUsers(Resource):
    @jwt_required
    def get(self) -> list:
        try:
            users = userService.showUsers()
            response = jsonify(ok = True, data = users)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response

@api.route("/api/v1/updateuser")
class UpdateUser(Resource):
    @jwt_required
    def put(self) -> dict:
        try:
            nickname = request.args.get('nickname')
            user_data = json.loads(request.data)
            user = userService.updateUser(nickname, user_data)
            response = jsonify(ok = True, data = user)
            response.status_code = 200
            return response
        except Exception as e:      
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response

@api.route("/api/v1/deleteuser")
class DeleteUser(Resource):
    @jwt_required
    def put(self) -> dict:
        try:
            nickname = request.args.get('nickname')
            user = userService.removeUser(nickname)
            response = jsonify(ok = True, data = user)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response