import sys
sys.path.append('../../')

from config.configFlaskJWTextended import *

@jwt.unauthorized_loader
def unauthorized_response(callback):
    response = jsonify(
        ok = False,
        message = "Missing Authorization Header"
    )
    response.status_code = 401

    return response