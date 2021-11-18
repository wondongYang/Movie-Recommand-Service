import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

const TMDB_API = process.env.VUE_APP_TMDB_API_KEY
const TMDB_BASEURL = 'https://api.themoviedb.org/3/movie/'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    login: false,
    HomeMovies: null,
    userMovieList: [],
  },
  mutations: {
    SET_LOGIN: function (state) {
      state.login = true
    },
    SET_LOGOUT: function (state) {
      state.login = false
    },

    SAVE_HOME_MOVIES: function (state, movies) {
      state.HomeMovies = movies
    },
    ADD_MY_LIST: function (state, item) {
      state.userMovieList.push(item)
    }

  },
  actions: {
    // JWT Token 받기
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`,
      }
      return config
    },

    setLogin: function ({commit}) {
      commit('SET_LOGIN')
    },
    
    setLogout: function ({commit}) {
      commit('SET_LOGOUT')
    },

    // Home.vue에서 보여줄 영화들 긁어오기
    getHomeMovies: function ({commit}) {
      axios({
        method: 'GET',
        // URL 필요에 따라 변경 (Django 서버로, 혹은 TMDB의 top rated, latest, ...)
        url: TMDB_BASEURL + 'popular',
        params: {
          api_key: TMDB_API,
          language: 'ko-KR',
        }
      })
      .then(response => {
        commit('SAVE_HOME_MOVIES', response.data.results)
      })
      .catch(error => {
        console.log(error)
      })
    },
    
  },
  modules: {
  },
  getters: {
    
  },
})
