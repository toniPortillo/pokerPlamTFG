def show_all_rooms(room_repository):
    list_of_rooms = room_repository.get_all()

    return list_of_rooms
