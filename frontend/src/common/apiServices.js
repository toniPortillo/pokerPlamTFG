import axios from '@/backend/vue-axios/axios'

const apiService = {
  post (resource, params) {
    return axios.post(`${resource}`, params)
  },
  get (resouce, id) {
    return axios.get(`${resouce}/${id}`).catch(error => {
      throw new Error(`ApiService ${error}`)
    })
  }
}

export default apiService

export const conversationsService = {
  create (params) {
    return apiService.post('/conversations', {
      name: params.conversation.name
    })
  },
  get (id) {
    return apiService.get('conversations', id)
  }
}

export const messagesService = {
  get (id) {
    if (typeof id !== 'string') {
      throw new Error('messagesService.get() conversation required to fetch messages')
    }
    return apiService.get('conversations', `${id}/messages`)
  },
  post (id, payload) {
    return apiService.post(`conversations/${id}/messages`, {
      content: payload.content,
      created_by: payload.created_by,
      conversation_id: payload.conversation_id,
      user_id: payload.user_id
    })
  }
}
