from flask_mongoengine.wtf import model_form

def userModel(userschema: object) -> dict:
    User = model_form(userschema)

    return User