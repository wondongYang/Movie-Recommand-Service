<template>
  <div class="d-flex flex-column align-items-center">
    <SearchMoviecard v-for="(movie, idx) in movies" :key="idx" :movie="movie" />
    <!-- <div v-for="(movie, idx) in movies" :key="idx">
      <MovieCard :movie="movie" />
    </div> -->
  </div>
</template>

<script>
import SearchMoviecard from '@/components/SearchMoviecard'
export default {
  name: 'SearchList',
  components: {
    SearchMoviecard,
  },
  props: {
    movies: Array,
  }
}
</script>

<style>

</style>