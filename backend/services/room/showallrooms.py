def show_all_rooms(room_repository, user_repository, room_dto, user_dto, formatted_user_list):
    list_of_rooms = room_repository.get_all()
    
    list_with_formatted_rooms = [] 

    for value in list_of_rooms:
        room_dto['room_name'] = value['room_name']
        room_dto['created_by'] = str(value['created_by']['id'])
        room_dto['room_date'] = value['room_date']
        room_dto['users'] = formatted_user_list(user_repository, value, user_dto)

        list_with_formatted_rooms.append(room_dto)
        
    return list_with_formatted_rooms
