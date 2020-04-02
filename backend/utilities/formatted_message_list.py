def formatted_message_list(message_repository: object, room: dict, message_dto: dict) -> dict:
    return [
        {
            'order_index': value['order_index'],
            'content': value['content'],
            'created_by': str(value['created_by']['id']),
            'message_date': value['message_date']
        }
        for value in room['messages']
    ]
