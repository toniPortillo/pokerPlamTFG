from flask_mongoengine.wtf import model_form

def userModel(userschema):
  User = model_form(userschema)

  return User