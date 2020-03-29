class RoomRepository():
    def __init__(self, room_entity: dict) -> None:
        self.room_entity = room_entity

    def create(self, room_data: dict) -> dict:
        room = self.room_entity
        
        saved_room = room(room_name = room_data['room_name'], users = [room_data['created_by']])
        saved_room.created_by = room_data['created_by']
        saved_room.save()

        return saved_room

    def find_by_room_name(self, room_name) -> dict:
        try:
            room = self.room_entity
            found_room = room.objects(room_name = room_name)

            return found_room[0]
        except Exception as e:
            raise Exception('Room does not exists')

    def get_all(self) -> list:
        room = self.room_entity

        all_the_rooms = room.objects.all()
        
        return all_the_rooms
    
    def add_user_to_list(self, room: dict, user: dict) -> dict:
        try:
            room_repository = self.room_entity

            room_with_the_user = room_repository.objects(room_name = room['room_name']).update_one(push__users = user)
            return room_with_the_user
        except Exception:
            raise Exception("Could not add user")

    def remove_user_from_list(self, room: dict, user: dict) -> dict:
        try:
            room_repository = self.room_entity

            room_without_the_user = room_repository.objects(room_name = room['room_name']).update_one(pull__users = user)
            return room_without_the_user
        except Exception:
            raise Exception("Could not remove user from room")

    def delete(self, room_name: str) -> int:
        try:
            room_repository = self.room_entity

            cleared_room = room_repository.objects(room_name = room_name).delete()
            return cleared_room
        except Exception:
            raise Exception("The room could not be deleted")