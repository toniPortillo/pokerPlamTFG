import sys
sys.path.append('../')

from services.estimate.index import *
estimate_services = IndexEstimateServices()

from config.configFlaskJWTextended import *
from utils.flaskJWTextend.unauthorized_loader import *

@api.route("/api/v1/estimate/create")
class CreateEstimate(Resource):
    @jwt_required
    def post(self) -> dict:
        try:
            room_name = request.args.get('room_name')
            created_by = request.args.get('created_by')
            estimate = json.loads(request.data)
            estimate_created = estimate_services.create_estimate(estimate, room_name, created_by)
            response = jsonify(ok = True, data = estimate_created)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response

@api.route("/api/v1/estimate/delete")
class DeleteEstimate(Resource):
    @jwt_required
    def put(self) -> dict:
        try:
            estimateid = request.args.get('estimateid')
            estimate_deleted = estimate_services.delete_estimate(estimateid)
            response = jsonify(ok = True, data = estimate_deleted)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response

@api.route("/api/v1/estimate/modifyfinalvalue")
class ModifyFinalValue(Resource):
    @jwt_required
    def put(self) -> dict:
        try:
            estimateid = request.args.get('estimateid')
            final_value = request.args.get('final_value')
            estimate_modified = estimate_services.modify_final_value(estimateid, final_value)
            response = jsonify(ok = True, data = estimate_modified)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response

@api.route("/api/v1/estimate/modifytitle")
class ModifyTitle(Resource):
    @jwt_required
    def put(self) -> dict:
        try:
            estimateid = request.args.get('estimateid')
            title = request.args.get('title')
            estimate_modified = estimate_services.modify_title(estimateid, title)
            response = jsonify(ok = True, data = estimate_modified)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response

@api.route("/api/v1/estimate/modifycommentary")
class ModifyComentary(Resource):
    @jwt_required
    def put(self) -> dict:
        try:
            estimateid = request.args.get('estimateid')
            commentary = request.args.get('commentary')
            estimate_modified = estimate_services.modify_commentary(estimateid, commentary)
            response = jsonify(ok = True, data = estimate_modified)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response