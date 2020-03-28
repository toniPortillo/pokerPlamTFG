class UserRepository():
    def __init__(self, userentity: dict) -> None:
        self.userentity = userentity

    def create(self, userdata: dict) -> dict:
        user = self.userentity
    
        saved_user = user(userid = userdata['userid'], username = userdata["username"], nickname = userdata["nickname"],
        password = userdata["password"], mail = userdata["mail"]).save()

        return saved_user
    def getAll(self) -> list:
        user = self.userentity
    
        return user.objects.all()

    def findOneByUsername(self, username: str) -> dict:
        try:
            user = self.userentity
    
            user_found = user.objects(username = username)
            return user_found[0]
        except Exception:
            raise Exception('User does not exists')
    

    def findOneByNickname(self, nickname: str) -> dict:
        try:
            user = self.userentity
    
            user_found = user.objects(nickname = nickname)
            return user_found[0]
        except Exception:
            raise Exception('User does not exists')
    

    def findOneByUserId(self, userid: str) -> dict:
        try:
            user = self.userentity

            user_found = user.objects(userid = userid)
            return user_found[0]
        except Exception:
            raise Exception('User does not exists')

    def find_by_mongo_id(self, primary_user_key:  str) -> dict:
        try:
            user = self.userentity
            user_found = user.objects(pk = primary_user_key)
            
            return user_found[0]
        except Exception:
            raise Exception('User does not exists')
    
    def updateDataUser(self, nickname: str, userdata: dict) -> dict:
        user = self.userentity
    
        updateduser = user.objects(nickname = nickname).update(username = userdata['username'], mail = userdata['mail'])
    
        return updateduser

    def removeByNickname(self, nickname: str) -> int:
        user = self.userentity

        return user.objects(nickname = nickname).delete()