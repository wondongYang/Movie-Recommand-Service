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
    HomeReviews: [],
    seletedMovie: null,
    HomeGenreMovies: {}
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
    },
    SAVE_GENRE_MOVIE_LIST: function (state, payload) {
      if (payload.data) {
        state.HomeGenreMovies[payload.genreName] = payload.data
      }
    }
  },
  actions: {
    // Auth
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
    },

    // 장르별 영화 가져오기
    getGenreMovies: function ({commit}, genre_name) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/top/${genre_name}/`
      })
      .then(response => {
        const payload = {
          genreName: genre_name,
          data: response.data
        }
        commit('SAVE_GENRE_MOVIE_LIST', payload)
      })
      .catch(error => {
        console.log(error)
      })
    }
    
  },
  modules: {
  },
  getters: {
    // HomeMoviesCut: function (state) {
    //   return state.HomeMovies.slice(0, 19)
    // },
    NewMovies: function (state) {
      const sixMonthAgo = dayjs().subtract(6, 'month').format("YYYY-MM-DD")
      console.log(sixMonthAgo)
      const ReleasedMovies = state.HomeMovies.filter(function(i) {
        return i.release_date <= sixMonthAgo
      })
      const NewMoviesList = _.orderBy(ReleasedMovies, 'release_date', 'desc').slice(0, 4)
      console.log(NewMoviesList)
      return NewMoviesList
    },

    ReviewsMovies: function (state) {
      const LargestReviewMovie = _.orderBy(state.HomeMovies, 'reviews.length', 'desc').slice(0, 4)
      console.log(LargestReviewMovie)
      return LargestReviewMovie
    },
    
    HomeGenreMovies: function (state) {
      return state.HomeGenreMovies
    },
  },
})
