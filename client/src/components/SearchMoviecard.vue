<template>
  <div class="card mb-3" style="max-width: 720px;">
    <router-link :to="{name: 'MovieDetail', params: {movieId: movie.id}}" :movie="movie" class="text-decoration-none link-dark">
    <div class="row g-0">
      <div class="col-md-4">
        <img :src="fullPosterPath" class="img-fluid rounded-start" alt="movie poster">
      </div>
      <div class="col-md-8">
        <div class="card-body text-start">
          <h5 class="card-title">{{ movie.title }}</h5>
          <p class="card-text"><small class="text-muted"><span v-for="(genre, id) in movie.genre_ids" :key="id">#{{genre.name}} </span></small></p>
          <br>
          <p class="card-text">{{ movie.overview | overviewAbbr }}</p>
          <p class="card-text text-end"><small class="text-muted"><span class="text-danger">❤</span> {{ movie.like_users.length }} | 📝 {{ movie.reviews.length }}</small></p>
        </div>
      </div>
    </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'SearchMoviecard',
  props: {
    movie: Object,
  },
  computed: {
    fullPosterPath: function () {
      const basePosterPath = 'https://image.tmdb.org/t/p/original'
      return (basePosterPath + this.movie.poster_path)
    }
  },
  filters: {
    // releaseDateRepr: function (datestring) {
    //   // YYYY-MM-DD >> YYYY년 M월 D일
    //   let [year, month, day] = datestring.split('-')
    //   month = parseInt(month)
    //   day = parseInt(day)
    //   return `${year}년 ${month}월 ${day}일`
    // },
    overviewAbbr: function (content) {
      return (content.length < 80 ? content : content.slice(0, 160) + ' ...')
    },
  },
}
</script>

<style>

</style>