import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

// const TMDB_API = process.env.VUE_APP_TMDB_API_KEY
// const TMDB_BASEURL = 'https://api.themoviedb.org/3/movie/'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    login: false,
    HomeMovies: null,
    seletedMovie: null,
  },
  mutations: {
    // Auth
    SET_LOGIN: function (state) {
      state.login = true
    },
    SET_LOGOUT: function (state) {
      state.login = false
    },

    // Movies
    SAVE_HOME_MOVIES: function (state, movies) {
      state.HomeMovies = movies
    },
    SELECT_MOVIE: function (state, movie) {
      state.seletedMovie = movie
    }
  },
  actions: {
    // Auth
    // JWT Token 받기
    // setToken: function () {
    //   const token = localStorage.getItem('jwt')
    //   const config = {
    //     Authorization: `JWT ${token}`,
    //   }
    //   return config
    // },
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
        // url: TMDB_BASEURL + 'popular',
        url: `${SERVER_URL}/movies/`
        // params: {
        //   api_key: TMDB_API,
        //   language: 'ko-KR',
        // }
      })
      .then(response => {
        commit('SAVE_HOME_MOVIES', response.data)
      })
      .catch(error => {
        console.log(error)
      })
    },
    selectMovie: function ({commit}, movie) {
      commit('SELECT_MOVIE', movie)
    }
    
  },
  modules: {
  },
  getters: {
    HomeMoviesCut: function (state) {
      return state.HomeMovies.slice(0, 19)
    }
  },
})
