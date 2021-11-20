import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'
import dayjs from 'dayjs'

// const TMDB_API = process.env.VUE_APP_TMDB_API_KEY
// const TMDB_BASEURL = 'https://api.themoviedb.org/3/movie/'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    login: false,
    HomeMovies: [],
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
    },
    NewMovies: function (state) {
      const today = dayjs().format("YYYY-MM-DD")
      console.log(today)
      const ReleasedMovies = _.filter(state.HomeMovies, 'release_date' <= today)
      console.log(ReleasedMovies)
      const NewMoviesList = _.orderBy(state.HomeMovies, 'release_date', 'desc')
      console.log(NewMoviesList.slice(0, 4))
      return NewMoviesList.slice(0, 4)
    },

    // PopularMovies: function (state) {
      // 리뷰 역추적 > 별점 평균 계산
    // }

    // ActionMovies: function (state) {
      // genre_ids안의 리스트 중에 28(action)이 존재한다면
    //   const ActionMovies = _.filter(state.HomeMovies, genre_ids[i] = 28)
    // }
  },
})
