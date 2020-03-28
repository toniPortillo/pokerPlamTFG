def show_all_rooms(room_repository, room_dto):
    list_of_rooms = room_repository.get_all()
    
    list_with_formated_rooms = [] 

    for value in list_of_rooms:
        room_dto['room_name'] = value['room_name']
        room_dto['created_by'] = str(value['created_by']['id'])
        room_dto['room_date'] = value['room_date']
        room_dto['users'] = str(value['users'][0]['id'])

        list_with_formated_rooms.append(room_dto)
        
    return list_with_formated_rooms
