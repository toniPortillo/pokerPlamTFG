def check_user_in_room(room: dict, nickname: dict) -> bool:
    flag = True
    for value in room['users']:
        if(value['nickname'] == nickname):
            flag = False

    return flag