<template>
  <div class="home">
    <!-- <button @click="getHomeMovies">Test Button</button> -->
    <br>
    <div v-if="HomeMovies" class="d-flex flex-wrap justify-content-evenly p-3">
      <MovieCard v-for="(movie, idx) in HomeMovies" :key="idx" :movie="movie" />
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
      return this.$store.state.HomeMovies
    }
  },
  // created: function () {
  //   this.$store.dispatch('getHomeMovies')
  // },
}
</script>
