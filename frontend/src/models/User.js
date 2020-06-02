export default class User {
  static from (obj) {
    console.log(obj)
    try {
      let user = {
        user_id: obj.id,
        conversation_ids: obj.conversationIds,
        name: obj.userName
      }
      return user
    } catch (_) {
      return null
    }
  }

  constructor ({ userId, conversationIds, userName }) {
    this.id = userId
    this.conversationIds = conversationIds
    this.username = userName
  }

  get isUser () {
    return this.user
  }
}
