<template>
  <div class="card m-3" style="width: 18rem; box-shadow: 0px 4px 5px 0px;">
    <router-link :to="{name: 'MovieDetail', params: {movieId: movie.id}}" :movie="movie" class="text-decoration-none link-dark">
    <img :src="fullPosterPath" class="card-img-top" alt="">
    <div class="card-body">
      <h3>{{movie.title}}</h3>
      <span v-for="(genre, id) in movie.genre_ids" :key="id">#{{genre.name}} </span>
      <div>
        <p class="card-text text-end"><small class="text-muted"> <span class="text-danger">❤</span> {{ movie.like_users.length }} | 📝 {{ movie.reviews.length }}</small></p>
      </div>
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