<template>
  <div>
    <div v-if="movie">
      <img :src="fullPosterPath" alt="Movie Poster" width="300">
      <h3>{{ movie.title }}</h3>
      <span v-for="(genre, genreidx) in movie.genres" :key="genreidx">{{ genre.name }} </span>
      <h5>{{ movie.release_date }}</h5>
      <p>{{ movie.overview }}</p>
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