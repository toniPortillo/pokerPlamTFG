from flask_mongoengine.wtf import model_form

def room_model(room_schema: object) -> dict:
    Room = model_form(room_schema)

    return Room