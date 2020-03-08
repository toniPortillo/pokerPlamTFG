class UserRepository():
  def __init__(self, userentity):
    self.userentity = userentity

  def create(self, userdata):
    user = self.userentity

    userSaved = user(username = userdata["username"], nickname = userdata["nickname"],
    password = userdata["password"], mail = userdata["mail"]).save()
    return userSaved

  def getAll(self):
    user = self.userentity
    
    return user.objects.all()

  def findOneByNickname(self, nickname):
    user = self.userentity
    
    return user.objects(nickname = nickname)

  def udpate(self, nickname, userdata):
    user = serf.userentity

    return user.objects(nickname = nickname).udpate(username = userdata['username'], mail = userdata['mail'])

  def removeByNickname(self, nickname):
    user = self.userentity

    return user.objects(nickname = nickname).delete()