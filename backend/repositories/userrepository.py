class UserRepository():
    def __init__(self, userentity: dict, userdto: dict) -> None:
        self.userentity = userentity
        self.userdto = userdto

    def create(self, userdata: dict) -> dict:
        user = self.userentity
    
        saveduser = user(userid = userdata['userid'], username = userdata["username"], nickname = userdata["nickname"],
        password = userdata["password"], mail = userdata["mail"]).save()
    
        self.userdto['id'] = saveduser['userid']
        self.userdto['username'] = saveduser['username']
        self.userdto['nickname'] = saveduser['nickname']
        self.userdto['password'] = saveduser['password']
        self.userdto['mail'] = saveduser['mail']

        return self.userdto

    def getAll(self) -> list:
        user = self.userentity
    
        return user.objects.all()

    def findOneByUsername(self, username: str) -> dict:
        try:
            user = self.userentity
    
            usertofound = user.objects(username = username)
            self.userdto['id'] = usertofound[0]['userid']
            self.userdto['username'] = usertofound[0]['username']
            self.userdto['nickname'] = usertofound[0]['nickname']
            self.userdto['password'] = usertofound[0]['password']
            self.userdto['mail'] = usertofound[0]['mail']
      
            return self.userdto 
        except Exception:
            raise Exception('User does not exists')
    

    def findOneByNickname(self, nickname: str) -> dict:
        try:
            user = self.userentity
    
            usertofound = user.objects(nickname = nickname)
            self.userdto['id'] = usertofound[0]['userid']
            self.userdto['username'] = usertofound[0]['username']
            self.userdto['nickname'] = usertofound[0]['nickname']
            self.userdto['password'] = usertofound[0]['password']
            self.userdto['mail'] = usertofound[0]['mail']
      
            return self.userdto 
        except Exception:
            raise Exception('User does not exists')
    

    def findOneByUserId(self, userid: str) -> dict:
        try:
            user = self.userentity
            usertofound = user.objects(userid = userid)
            return usertofound
        except Exception:
            raise Exception('User does not exists')

    def updateDataUser(self, nickname: str, userdata: dict) -> dict:
        user = self.userentity
    
        updateduser = user.objects(nickname = nickname).update(username = userdata['username'], mail = userdata['mail'])
    
        return updateduser

    def removeByNickname(self, nickname: str) -> int:
        user = self.userentity

        return user.objects(nickname = nickname).delete()