<template>
  <div id="carouselExampleSlidesOnly" class="carousel slide bg-dark" data-bs-ride="carousel">
    <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleSlidesOnly" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button v-for="(movie, btnidx) in movies.slice(1)" :key="btnidx" type="button" data-bs-target="#carouselExampleSlidesOnly" :data-bs-slide-to="btnidx + 1" :aria-label="'Slide ' + String(btnidx)"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <div class="d-flex justify-content-center">
        <HomeCarousel2Card :movie="movies[0]" />
      </div>
      <!-- <MovieCard :movie="movies[0]" /> -->
    </div>
    <div class="carousel-item" v-for="(movie, idx) in movies.slice(1)" :key="idx">
      <div class="d-flex justify-content-center">
        <HomeCarousel2Card :movie="movie" />
      </div>
      <!-- <MovieCard :movie="movie" /> -->
    </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleSlidesOnly" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleSlidesOnly" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
  </div>
</div>
</template>

<script>
// import MovieCard from '@/components/MovieCard'
import HomeCarousel2Card from '@/components/HomeCarousel2Card'
export default {
  name: 'HomeCarousel2',
  components: {
    // MovieCard,
    HomeCarousel2Card,
  },
  props: {
    movies: Array,
  }
}

</script>

<style>

</style>