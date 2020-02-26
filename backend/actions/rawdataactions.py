import sys
sys.path.append("../")

from config.configApp import *
from services.raw.index import *
rawService = IndexRawServices()

@api.route("/api/v1/data")
class Data(Resource):
    @api.doc('get_all_data')
    def get(self):
        try:
            contacts = rawService.showData()
            return dumps(contacts)
        except Exception as e:
            return dumps({'error': str(e)})
    @api.doc('post_data')
    def post(self):
        try:
            data = json.loads(request.data)
            status = rawService.create(data)
            return dumps({'message': 'SUCCESS'})
        except Exception as e:
            return dumps({'error': str(e)})
