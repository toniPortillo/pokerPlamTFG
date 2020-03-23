from flask_mongoengine.wtf import model_form

def message_model(message_schema: object) -> dict:
    Message = model_form(message_schema)

    return Message