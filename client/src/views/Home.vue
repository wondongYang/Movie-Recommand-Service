<template>
  <div class="home">
    <div>
      <p> 메인 화면이 들어갈 공간입니다. (Carousel이나 Wallpaper 등...)</p>
      <p> Soy Source </p>
    </div>
    <br>
    <div>
      <h3>최근 개봉작</h3>
      <div v-if="$store.getters.NewMovies" class="d-flex flex-wrap justify-content-evenly p-3">
        <MovieCard v-for="(movie, idx) in NewMovies" :key="idx" :movie="movie" />
      </div>
      <hr>
      <h3>리뷰가 많이 달린 영화</h3>
      <div v-if="$store.getters.ReviewsMovies" class="d-flex flex-wrap justify-content-evenly p-3">
        <MovieCard v-for="(movie, idx) in ReviewsMovies" :key="idx" :movie="movie" />
      </div>
      <hr>

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
import { mapGetters } from 'vuex'
export default {
  name: 'Home',
  components: {
    MovieCard,
  },
  computed: {
    NewMovies: function () {
      return this.$store.getters.NewMovies
    },
    ReviewsMovies: function () {
      return this.$store.getters.ReviewsMovies
    },
    ...mapGetters(['HomeGenreMovies',])
    // server/movies/views.py 참조
  },
  // beforeCreate: function () {
  //   // 영화 들고 오기
  //   this.$store.dispatch('getHomeMovies')
  // }
  // created: function () {
  //   this.$store.dispatch('getHomeMovies')
  // },
}
</script>
