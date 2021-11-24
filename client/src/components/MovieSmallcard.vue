<template>
  <div class="card m-3 box-shade link-dark" style="width: 10rem;">
    <router-link :to="{name: 'MovieDetail', params: {movieId: movie.id}}" :movie="movie" class="text-decoration-none link-dark">
    <img :src="fullPosterPath" class="card-img-top" alt="Movie Poster">
    <div class="card-body">
      <p class="text-decoration-none">{{movie.title}}</p>
    </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  computed: {
    fullPosterPath: function () {
      const basePosterPath = 'https://image.tmdb.org/t/p/original'
      return (basePosterPath + this.movie.poster_path)
    }
  }
}
</script>

<style>

</style>