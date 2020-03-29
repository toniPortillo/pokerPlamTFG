def check_creator(room: dict, user: dict) -> bool:
    print(room['created_by']['id'])
    print(user['id'])
    if(room['created_by']['id'] == user['id']):
        return False
    else: 
        return True