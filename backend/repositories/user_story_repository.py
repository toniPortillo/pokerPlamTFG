class UserStoryRepository():
    def __init__(self, room_entity: dict, user_story_entity: dict) -> None:
        self.room_entity = room_entity
        self.user_story_entity = user_story_entity

    def create(self, room_name: str, user_story_data: dict) -> dict:
        try:
            room = self.room_entity
            user_story = self.user_story_entity
            found_room = room.objects(room_name = room_name).first()
            saved_user_story = user_story(storyid = user_story_data['storyid'], order_index = len(found_room['user_stories']) + 1, 
            story_title = user_story_data['story_title'], role = user_story_data['role'], reason = user_story_data['reason'],
            estimate = int(user_story_data['estimate']), importance = int(user_story_data['importance']), 
            acceptance_criteria = user_story_data['acceptance_criteria'], created_by = user_story_data['created_by'])
            found_room.user_stories.append(saved_user_story)
            found_room.save()

            return found_room

        except Exception as e:
            raise Exception('The user story was not created')

    def delete_user_story(self, room_name: str, storyid: str) -> dict:
        try:
            room = self.room_entity
            user_story = self.user_story_entity
            found_room = room.objects(room_name = room_name).first()
            found_user_story = room.objects(user_stories__match={"storyid": storyid}).first()
            for value in found_user_story['user_stories']:
                if(value['storyid'] == storyid):
                    print(value['storyid'])
                    found_room.user_stories.remove(value)
                    found_room.save()
                    return found_room
        except Exception as e:
            raise Exception('User story was not removed')