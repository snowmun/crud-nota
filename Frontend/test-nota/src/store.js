import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLoggedIn: false,
    user: {
        id: null,
        nombre_usuario: null,
    },
    token: null
  },
  mutations: {
    setUsername(state, username) {
        state.user.nombre_usuario = username;
    },
    setToken(state, token) {
        state.token = token;
    },
    login (state, user) {
      state.isLoggedIn = true
      state.user = user
    },
    logout (state) {
      state.isLoggedIn = false
      state.user = null
      state.token = null
    },
    setUserId(state, id) {
        state.user.id = id;
    }
  },
  actions: {
    loginUser ({ commit }, user) {
        commit('login', user)
        commit('setToken', user.token)
        commit('setUsername', user.nombre_usuario)
        commit('setUserId', user.id) 
      },
    logoutUser ({ commit }) {
      commit('logout')
      commit('setToken', null)
      commit('setUsername', null)
    }
  }
})
