import Vue from 'vue'
import { conversationsService, messagesService } from '@/common/apiServices'
import {
  MESSAGE_CREATE,
  FETCH_CONVERSATION,
  FETCH_MESSAGES,
  CONVERSATION_PUBLISH,
  CONVERSATION_RESET_STATE
} from './actions-type'
import { SET_CONVERSATION, RESET_STATE, SET_MESSAGES } from './mutations-type'

const initialState = {
  conversation: {
    name: ''
  },
  messages: []
}

export const state = Object.assign({}, initialState)

export const actions = {
  [FETCH_CONVERSATION] (context, conversationId, prevConversation) {
    if (prevConversation !== undefined) {
      return context.commit(SET_CONVERSATION, prevConversation)
    }
    return conversationsService.get(conversationId).then(({data}) => {
      context.commit(SET_CONVERSATION, data)
      return data
    })
  },
  [FETCH_MESSAGES] (context, conversationId) {
    return messagesService.get(conversationId).then(({ data }) => {
      context.commit(SET_MESSAGES, data)
    })
  },
  [MESSAGE_CREATE] (context, payload) {
    console.log(payload)
    return messagesService.post(payload.id, payload.message).then(() => {
      context.dispatch(FETCH_MESSAGES, payload.id)
    })
  },
  [CONVERSATION_PUBLISH] ({ state }) {
    return conversationsService.create(state)
  },
  [CONVERSATION_RESET_STATE] ({commit}) {
    commit(RESET_STATE)
  }
}

export const mutations = {
  [SET_CONVERSATION] (state, conversation) {
    state.conversation = conversation
  },
  [SET_MESSAGES] (state, messages) {
    state.messages = messages
  },
  [RESET_STATE] () {
    for (let f in state) {
      Vue.set(state, f, initialState[f])
    }
  }
}

export const getters = {
  conversation (state) {
    return state.conversation
  },
  messages (state) {
    return state.messages
  }
}

export default {
  state,
  actions,
  mutations,
  getters
}
