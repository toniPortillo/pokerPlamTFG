class RoomRepository():
    def __init__(self, room_entity: dict, room_dto: dict) -> None:
        self.room_entity = room_entity
        self.room_dto = room_dto

    def create(self, room_data: dict) -> dict:
        room = self.room_entity
        print(room_data)
        saved_room = room(room_name = room_data['room_name'], created_by = room_data['created_by']).save()
        
        self.room_dto['room_name'] = saved_room[0]['room_name']
        self.room_dto['created_by'] = saved_room[0]['created_by']
        self.room_dto['room_date'] = saved_room[0]['room_date']
        self.room_dto['users'] = []
        self.room_dto['messages'] = []

        return self.room_dto