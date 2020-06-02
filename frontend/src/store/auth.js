import * as MutationTypes from './mutations-type'

let initialState = {}
if (JSON.parse(localStorage.getItem('user')) === null) {
  initialState = {
    user: null
  }
} else {
  const user = JSON.parse(localStorage.getItem('user'))
  initialState = {
    user: {
      _id: user._id,
      conversations_ids: user.conversations_ids,
      name: user.name
    }
  }
}

export const state = Object.assign({}, initialState)

const mutations = {
  [MutationTypes.SIGNUP] (state) {
    state.user = JSON.parse(localStorage.getItem('user'))
  },
  [MutationTypes.LOGIN] (state) {
    state.user = JSON.parse(localStorage.getItem('user'))
  },
  [MutationTypes.LOGOUT] (state) {
    state.user = null
  }
}

const actions = {
  signup ({ commit }) {
    commit(MutationTypes.SIGNUP)
  },

  login ({ commit }) {
    commit(MutationTypes.LOGIN)
  },

  logout ({ commit }) {
    commit(MutationTypes.LOGOUT)
  }
}

const getters = {
  currentUser (state) {
    return state.user
  }
}

export default {
  state,
  mutations,
  getters,
  actions
}
