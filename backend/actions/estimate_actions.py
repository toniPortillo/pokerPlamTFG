import sys
sys.path.append('../')

from services.estimate.index import *
estimate_services = IndexEstimateServices()

from config.configFlaskJWTextended import *
from utils.flaskJWTextend.unauthorized_loader import *

@api.route("/api/v1/estimate/create")
class CreateEstimate(Resource):
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