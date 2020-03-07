class UserRepository():
  def __init__(self, userentity):
    self.userentity = userentity

  def create(self, userdata):
    print(userdata)
    user = self.userentity
    #user.username = userdata["username"]
    #user.nickname = userdata["nickname"]
    #user.password = userdata["password"]
    #user.mail = userdata["mail"]
    userSaved = user(username = userdata["username"], nickname = userdata["nickname"],
    password = userdata["password"], mail = userdata["mail"]).save()
    return userSaved

  def getAll(self):
    user = self.userentity
    
    return user.objects.all()