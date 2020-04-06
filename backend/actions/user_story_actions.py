import sys
sys.path.append('../')

from services.user_story.index import *
user_story_services = IndexUserStoryServices()

from config.configFlaskJWTextended import *
from utils.flaskJWTextend.unauthorized_loader import *

@api.route("/api/v1/userstory/create")
class CreateUserStory(Resource):
    @jwt_required
    def post(self ) -> dict:
        try:
            room_name = request.args.get('room_name')
            created_by = request.args.get('created_by')
            user_story = json.loads(request.data)
            created_user_story = user_story_services.create_user_story(user_story, room_name, created_by)
            response = jsonify(ok = True, data = created_user_story)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response

@api.route("/api/v1/userstory/showuserstories")
class ShowUserStories(Resource):
    @jwt_required
    def get(self) -> dict:
        try:
            room_name = request.args.get('room_name')
            user_stories_obtained = user_story_services.get_room_user_stories(room_name)
            response = jsonify(ok = True, data = user_stories_obtained)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response

@api.route("/api/v1/userstory/delete")
class DeleteUserStory(Resource):
    @jwt_required
    def put(self) -> dict:
        try:
            room_name = request.args.get('room_name')
            storyid = request.args.get('storyid')
            updated_user_story = user_story_services.delete_user_story(room_name, storyid)
            response = jsonify(ok = True, data = updated_user_story)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response

@api.route("/api/v1/userstory/modify")
class ModifyUserStory(Resource):
    @jwt_required
    def put(self) -> dict:
        try:
            storyid = request.args.get('storyid')
            user_story_data = json.loads(request.data)
            updated_user_story = user_story_services.modify_user_story(storyid, user_story_data)
            response = jsonify(ok = True, data = updated_user_story)
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify(ok = False, message = str(e))
            response.status_code = 500
            return response