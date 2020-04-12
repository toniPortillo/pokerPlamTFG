import sys
sys.path.append('../')

from services.vote.index import *
vote_services = IndexVoteServices()

from config.configFlaskJWTextended import *
from utils.flaskJWTextend.unauthorized_loader import *

@api.route("/api/v1/vote/create")
class CreateVote(Resource):
    def post(self) -> dict:
        try:
            room_name = request.args.get('room_name')
            estimateid = request.args.get('estimateid')
            nickname = request.args.get('nickname')
            vote = json.loads(request.data)
            vote_created = vote_services.create_vote(vote, room_name, estimateid, nickname)
            response = jsonify(ok = True, data = vote_created)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response