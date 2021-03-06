import sys
sys.path.append('../')

from services.vote.index import *
vote_services = IndexVoteServices()

from config.configFlaskJWTextended import *
from utils.flaskJWTextend.unauthorized_loader import *

@api.route("/api/v1/vote/create")
class CreateVote(Resource):
    @jwt_required
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

@api.route("/api/v1/vote/showvotes")
class ShowVotes(Resource):
    @jwt_required
    def get(self) -> dict:
        try:
            room_name = request.args.get('room_name')
            estimateid = request.args.get('estimateid')
            get_estimate = vote_services.show_votes(room_name, estimateid)
            response = jsonify(ok = True, data = get_estimate)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response

@api.route("/api/v1/vote/delete")
class DeleteVote(Resource):
    @jwt_required
    def put(self) -> dict:
        try:
            room_name = request.args.get('room_name')
            estimateid = request.args.get('estimateid')
            nickname = request.args.get('nickname')
            get_estimate = vote_services.delete_vote(room_name, estimateid, nickname)
            response = jsonify(ok = True, data = get_estimate)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response