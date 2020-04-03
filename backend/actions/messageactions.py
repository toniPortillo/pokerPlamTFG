import sys
sys.path.append('../')

from services.message.index import *
message_services = IndexMessageServices()

from config.configFlaskJWTextended import *
from utils.flaskJWTextend.unauthorized_loader import *

@api.route("/api/v1/message/create")
class CreateMessage(Resource):
    @jwt_required
    def post(self) -> dict:
        try:
            room_name = request.args.get('room_name')
            created_by = request.args.get('created_by')
            message = json.loads(request.data)
            created_message = message_services.create_message(message, room_name, created_by)
            response = jsonify(ok = True, data = created_message)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response

@api.route("/api/v1/message/showmessages")
class ShowMessages(Resource):
    @jwt_required
    def get(self) -> dict:
        try:
            room_name = request.args.get('room_name')
            messages_obtained = message_services.get_room_messages(room_name)
            response = jsonify(ok = True, data = messages_obtained)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response