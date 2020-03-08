class UserRepository():
  def __init__(self, userentity, userdto):
    self.userentity = userentity
    self.userdto = userdto

  def create(self, userdata):
    user = self.userentity
    
    saveduser = user(username = userdata["username"], nickname = userdata["nickname"],
    password = userdata["password"], mail = userdata["mail"]).save()
    
    self.userdto['username'] = saveduser['username']
    self.userdto['nickname'] = saveduser['nickname']
    self.userdto['password'] = saveduser['password']
    self.userdto['mail'] = saveduser['mail']

    return self.userdto

  def getAll(self):
    user = self.userentity
    
    return user.objects.all()

  def findOneByNickname(self, nickname):
    user = self.userentity
    
    usertofound = user.objects(nickname = nickname)
    self.userdto['username'] = usertofound[0]['username']
    self.userdto['nickname'] = usertofound[0]['nickname']
    self.userdto['password'] = usertofound[0]['password']
    self.userdto['mail'] = usertofound[0]['mail']

    return self.userdto 

  def updateDataUser(self, nickname, userdata):
    user = self.userentity
    
    updateduser = user.objects(nickname = nickname).update(username = userdata['username'], mail = userdata['mail'])
    
    return updateduser

  def removeByNickname(self, nickname):
    user = self.userentity

    return user.objects(nickname = nickname).delete()