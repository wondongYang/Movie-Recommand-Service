<template>
  <div>
    <!-- 최초에 로드되지 않은 movie(null)를 참조할 때 error가 발생하는 것을 막기 위해 v-if를 사용합니다-->
    <div v-if="movie" class="container">
      <div class="d-flex justify-content-between">
        <button @click="$router.go(-1)" class="btn btn-secondary me-auto" >뒤로</button>
        <div>좋아요 수: {{ count }}</div>
      </div>
      <div v-if="like" class="d-flex justify-content-end">
        <button @click="LikeMovie(movieId)" class="btn btn-link">
          <i class="fa-solid fa-thumbs-down"></i>
        </button>
      </div>
      <div v-else class="d-flex justify-content-end">
        <button @click="LikeMovie(movieId)" class="btn btn-link">
          <i class="fa-solid fa-thumbs-up"></i>
        </button>
      </div>
      <hr>
      <div class="row">
        <div class="col-3">
          <img :src="fullPosterPath" alt="Movie Poster" class="img-fluid">

        </div>
        <div class="col-9">
          <h2 class="fs-2 text-start">{{ movie.title }}</h2>
          <p class="text-end">
          <span v-for="(genre, genreidx) in movie.genre_ids" :key="genreidx" class="text-end">{{ genre.name }} | </span>
          </p>
          <p class="text-end fs=4">{{ movie.release_date|releaseDateRepr }}</p>
          <br>
          <p class="text-start">{{ movie.overview }}</p>
        </div>
      </div>
      <hr>
      <div v-for="(review, id) in movie.reviews" :key="id">
        <MovieDetailReview :review="review" />
      </div>
      <div class="d-flex">

      <div class="ms-auto" v-if="login">
        <router-link :to="{name: 'ReviewForm', query: {movieTitle: movie.title}}" class="btn btn-primary ms-auto" :movie="movie">리뷰 작성하기</router-link>
      </div>
      <div class="ms-auto" v-else>
        <router-link :to="{name: 'Login'}" :movie="movie">리뷰를 작성하려면 로그인하세요</router-link>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'
import MovieDetailReview from '@/components/MovieDetailReview'
// const TMDB_BASEURL = 'https://api.themoviedb.org/3/movie/'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
// const TMDB_API = process.env.VUE_APP_TMDB_API_KEY
export default {
  name: 'MovieDetail',
  components: {
    MovieDetailReview,
  },
  data: function () {
    return {
      movieId: this.$route.params.movieId,
      movie: null,
      // like: this.movie.like_users,
      like: null,
      count: null,
      username: null,
    }
  },
  props: {
    // movieId: Number,
  },
  methods: {
    isUsername(element) {
      if(element.username === this.username) {
        return true
      }
    },
    getMovieDetail: function (movieId) {
      axios({
        method: 'GET',
        // url: TMDB_BASEURL + movieId,
        url: `${SERVER_URL}/movies/${movieId}/`,
        // params: {
        //   api_key: TMDB_API,
        //   language: 'ko-KR'
        // }
      })
      .then(response => {
        this.movie = response.data
        this.count = this.movie.like_users.length
        this.username = this.$store.state.username
        this.like = this.movie.like_users.some((element) => {
          if(element.username === this.username) {
            return true
          }
        })
        this.$store.dispatch('selectMovie', this.movie)
      })
    },
    LikeMovie: function (movieId) {
      const like = {
        movie: this.$route.params.movieId,
        like: this.like,
      }
      this.setToken()
      axios({
        method: 'POST',
        url: `${SERVER_URL}/movies/${movieId}/likes/`,
        headers: this.$store.state.tokenStr,
        data: like,     
      })
      .then((response) => {
        console.log(this.movie.like_users)
        console.log(this.username)
        this.like = !this.like
        this.count = response.data.count
      })
    }, 
    ...mapActions(['setToken',])
  },
  computed: {
    fullPosterPath: function () {
      const basePosterPath = 'https://image.tmdb.org/t/p/original'
      return (basePosterPath + this.movie.poster_path)
    },
    login: function () {
      return this.$store.state.login
    },
  },
  mounted: function () {
    this.getMovieDetail(this.movieId)
  },
  filters: {
    releaseDateRepr: function (datestring) {
      // YYYY-MM-DD >> YYYY년 M월 D일
      let [year, month, day] = datestring.split('-')
      month = parseInt(month)
      day = parseInt(day)
      return `${year}년 ${month}월 ${day}일`
    }
  },
  
}
</script>

<style>

</style>