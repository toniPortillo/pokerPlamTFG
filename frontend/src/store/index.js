import Vue from 'vue'
import Vuex from 'vuex'

import auth from './auth'
import conversation from './conversation'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth,
    conversation
  }
})
