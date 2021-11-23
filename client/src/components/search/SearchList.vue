<template>
  <div>
    <MovieCard v-for="(movie, idx) in movies" :key="idx" :movie="movie" />
    <!-- <div v-for="(movie, idx) in movies" :key="idx">
      <MovieCard :movie="movie" />
    </div> -->
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
export default {
  name: 'SearchList',
  components: {
    MovieCard,
  },
  props: {
    movies: Array,
  }
}
</script>

<style>

</style>