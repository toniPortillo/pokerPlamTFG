import sys
sys.path.append('../')

from services.room.index import *
room_services = IndexRoomServices()

from config.configFlaskJWTextended import *
from utils.flaskJWTextend.unauthorized_loader import *

@api.route("/api/v1/room/create")
class CreateRoom(Resource):
    def post(self) -> dict:
        try:
            primary_user_key = request.args.get('primary_user_key')
            room = json.loads(request.data)
            created_room = room_services.create_room(room, primary_user_key)
            response = jsonify(ok = True, data = created_room)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response

@api.route("/api/v1/room/show")
class ShowRoom(Resource):
    def get(self) -> dict:
        try:
            room_name = request.args.get('room_name')
            found_room = room_services.show_room(room_name)
            response = jsonify(ok = True, data = found_room)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response

@api.route("/api/v1/room/showallrooms")
class ShowAllRooms(Resource):
    def get(self) -> list:
        try:
            list_all_rooms = room_services.show_all_rooms()
            
            response = jsonify(ok = True, data = list_all_rooms)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response
