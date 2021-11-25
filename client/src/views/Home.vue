<template>
  <div class="home">
    <div>
      <div class="bg-dark">NEW</div>
      <HomeCarousel2 :movies="latestMovies" />
      <hr>
      <h3>좋아요를 많이 받은 영화</h3>
      <HomeCarousel />
      <hr>
    </div>
    <br>
    <div>
      <!-- <div v-if="latestMovies" class="d-flex flex-wrap justify-content-evenly p-3">
        <MovieCard v-for="(movie, idx) in latestMovies" :key="idx" :movie="movie" />
      </div>
      <hr> -->
      <!-- <div v-if="largestReviewMovies" class="d-flex flex-wrap justify-content-evenly p-3">
        <MovieCard v-for="(movie, idx) in largestReviewMovies" :key="idx" :movie="movie" />
      </div>
      <hr> -->
      <div class="container">
        <h2>장르별 영화</h2>
        <div>
          <h3 class="text-start">액션</h3>
          <div v-if="HomeGenreMovies.action" class="d-flex flex-wrap justify-content-evenly p-3">
            <MovieCard v-for="(movie, idx) in HomeGenreMovies.action" :key="idx" :movie="movie" />
          </div>
        </div>
        <div>
          <h3 class="text-start">드라마</h3>
          <div v-if="HomeGenreMovies.drama" class="d-flex flex-wrap justify-content-evenly p-3">
            <MovieCard v-for="(movie, idx) in HomeGenreMovies.drama" :key="idx" :movie="movie" />
          </div>
        </div>
        <div>
          <h3 class="text-start">애니메이션</h3>
          <div v-if="HomeGenreMovies.animation" class="d-flex flex-wrap justify-content-evenly p-3">
            <MovieCard v-for="(movie, idx) in HomeGenreMovies.animation" :key="idx" :movie="movie" />
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
// @ is an alias to /src
// import {mapActions} from 'vuex'
import MovieCard from '@/components/MovieCard'
import HomeCarousel from '@/components/HomeCarousel'
import HomeCarousel2 from '@/components/HomeCarousel2'
import { mapGetters } from 'vuex'
export default {
  name: 'Home',
  components: {
    MovieCard,
    HomeCarousel,
    HomeCarousel2,
  },
  computed: {
    ...mapGetters(['latestMovies','largestReviewMovies','HomeGenreMovies',])
  },
  created: function () {
    this.$store.dispatch('getlatestMovies')
    this.$store.dispatch('getlargestReviewMovies')
  },
}
</script>
