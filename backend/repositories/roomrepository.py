class RoomRepository():
    def __init__(self, room_entity: dict, room_dto: dict) -> None:
        self.room_entity = room_entity
        self.room_dto = room_dto

    def create(self, room_data: dict) -> dict:
        room = self.room_entity
        
        saved_room = room(room_name = room_data['room_name'], users = [room_data['created_by']])
        saved_room.created_by = room_data['created_by']
        saved_room.save()
        
        self.room_dto['room_name'] = saved_room['room_name']
        self.room_dto['created_by'] = str(saved_room['created_by']['id'])
        self.room_dto['room_date'] = saved_room['room_date']
        self.room_dto['users'] = str(saved_room['users'])
        self.room_dto['messages'] = [{}]

        return self.room_dto