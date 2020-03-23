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
            user_id = request.args.get('user_id')
            room = json.loads(request.data)
            created_room = room_services.create_room(room, user_id)
            response = jsonify(ok = True, data = created_room)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response