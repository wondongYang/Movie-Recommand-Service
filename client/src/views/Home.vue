<template>
  <div class="home">
    <div>
      <p> 메인 화면이 들어갈 공간입니다. (Carousel이나 Wallpaper 등...)</p>
      <p> Soy Source </p>
    </div>
    <br>
    <div>
      <h3>인기 영화들</h3>
      <div v-if="HomeMovies" class="d-flex flex-wrap justify-content-evenly p-3">
        <MovieCard v-for="(movie, idx) in HomeMovies" :key="idx" :movie="movie" />
      </div>

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
    HomeMovies: function () {
      return this.$store.state.HomeMovies.slice(0, 19)
    }
  },
  // created: function () {
  //   this.$store.dispatch('getHomeMovies')
  // },
}
</script>
