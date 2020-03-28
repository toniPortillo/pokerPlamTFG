class RoomRepository():
    def __init__(self, room_entity: dict) -> None:
        self.room_entity = room_entity

    def create(self, room_data: dict) -> dict:
        room = self.room_entity
        
        saved_room = room(room_name = room_data['room_name'], users = [room_data['created_by']])
        saved_room.created_by = room_data['created_by']
        saved_room.save()

        return saved_room

    def find_by_room_name(self, room_name):
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