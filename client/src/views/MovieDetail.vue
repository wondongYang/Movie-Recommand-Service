<template>
  <div>
    <!-- 최초에 로드되지 않은 movie(null)를 참조할 때 error가 발생하는 것을 막기 위해 v-if를 사용합니다-->
    <div v-if="movie" class="container">
      <div class="row">
        <div class="col-3">
          <img :src="fullPosterPath" alt="Movie Poster" class="img-fluid">


        </div>
        <div class="col-9">
          <h2 class="text-start">{{ movie.title }}</h2>
          <p class="text-end">
          <span v-for="(genre, genreidx) in movie.genres" :key="genreidx" class="text-end">{{ genre.name }} </span>
          </p>
          <h5 class="text-end">{{ movie.release_date }}</h5>
          <br>
          <p>{{ movie.overview }}</p>
        </div>
      </div>
      <MovieDetailReview :movieId="movie.id" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieDetailReview from '@/components/MovieDetailReview'
const TMDB_BASEURL = 'https://api.themoviedb.org/3/movie/'
const TMDB_API = process.env.VUE_APP_TMDB_API_KEY
export default {
  name: 'MovieDetail',
  components: {
    MovieDetailReview,
  },
  data: function () {
    return {
      movieId: this.$route.params.movieId,
      movie: null
    }
  },
  props: {
    // movieId: Number,
  },
  methods: {
    getMovieDetail: function (movieId) {
      axios({
        method: 'GET',
        url: TMDB_BASEURL + movieId,
        params: {
          api_key: TMDB_API,
          language: 'ko-KR'
        }
      })
      .then(response => {
        this.movie = response.data
      })
    }
  },
  computed: {
    fullPosterPath: function () {
      const basePosterPath = 'https://image.tmdb.org/t/p/original'
      return (basePosterPath + this.movie.poster_path)
    }
  },
  mounted: function () {
    this.getMovieDetail(this.movieId)
  }
  
}
</script>

<style>

</style>