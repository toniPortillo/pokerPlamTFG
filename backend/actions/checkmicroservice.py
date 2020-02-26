import sys
sys.path.append("../")

from config.configApp import *


@api.route("/api/v1/check_microservice")
class Hello(Resource):
  def get(self):
    return "Welcome to Poc microservice!"
