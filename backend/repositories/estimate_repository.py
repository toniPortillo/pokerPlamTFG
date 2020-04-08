class EstimateRepository():
    def __init__(self, room_entity: dict, estimate_entity: dict) -> None:
        self.room_entity = room_entity
        self.estimate_entity = estimate_entity

    def create(self, room_name: str, estimate_data: dict) -> dict:
        try:
            room = self.room_entity
            estimate = self.estimate_entity
            found_room = room.objects(room_name = room_name).first()
            
            saved_estimate = estimate(estimateid = estimate_data['estimateid'], title = estimate_data['title'], 
            final_value = 0, commentary = estimate_data['commentary'], created_by = estimate_data['created_by'])
            
            found_room.estimates.append(saved_estimate)
            found_room.save()

            return found_room
        except Exception as e:
            raise Exception('The estimate was not created')