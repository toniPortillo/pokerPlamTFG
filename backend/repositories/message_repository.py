class MessageRepository():
    def __init__(self, room_entity: dict, message_entity: dict) -> None:
        self.room_entity = room_entity
        self.message_entity = message_entity
    
    def create(self, room_name: str, message_data: dict) -> dict:
        try:
            room = self.room_entity
            message = self.message_entity
            found_room = room.objects(room_name = room_name).first()
            saved_message = message(order_index = len(found_room['messages']) + 1, content = message_data['content'],
            created_by = message_data['created_by'])
            found_room.messages.append(saved_message)
            found_room.save()
            
            return found_room
        except Exception as e:
            raise Exception('The message was not created')