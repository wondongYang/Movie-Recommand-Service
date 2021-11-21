<template>
  <div class="home">
    <div>
      <p> 메인 화면이 들어갈 공간입니다. (Carousel이나 Wallpaper 등...)</p>
      <p> Soy Source </p>
    </div>
    <br>
    <div>
      <!-- <h3>인기 영화들</h3>
      <div v-if="$store.getters.NewMovies" class="d-flex flex-wrap justify-content-evenly p-3">
        <MovieCard v-for="(movie, idx) in NewMovies" :key="idx" :movie="movie" />
      </div> -->
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
      <h3>장르별 영화</h3>
      <p>액션</p>
      <!-- <div v-if="$store.getters.ActionMovies" class="d-flex flex-wrap justify-content-evenly p-3">
        <MovieCard v-for="(movie, idx) in ActionMovies" :key="idx" :movie="movie" />
      </div> -->
    </div>

  </div>
</template>

<script>
// @ is an alias to /src
// import {mapActions} from 'vuex'
import MovieCard from '@/components/MovieCard'

export default {
  name: 'Home',
  components: {
    MovieCard,
  },
  computed: {
    // HomeMoviesCut: function () {
    //   return this.$store.getters.HomeMoviesCut
    // },
    NewMovies: function () {
      return this.$store.getters.NewMovies
    },
    ReviewsMovies: function () {
      return this.$store.getters.ReviewsMovies
    },
    // ActionMovies: function () {
    //   return this.$store.getters.ActionMovies
    // },
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
