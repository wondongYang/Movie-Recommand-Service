<template>
  <div id="Carousel" class="carousel carousel-dark slide" data-bs-ride="carousel">
  <div class="carousel-indicators">
    <button v-for="(movie, idx) in latestMovies" :key="idx"
     type="button" data-bs-target="#Carousel" :data-bs-slide-to="idx" :aria-label="`Slide ${idx}`"
     :class="{active: idx === 0}" :aria-current="{true: idx === 0}"></button>
  </div>
  <div class="carousel-inner">
    <div v-for="(movie, idx) in latestMovies" :key="idx"
     :class="{carouselItem_active: idx === 0}" data-bs-interval="10000">
      <img :src="fullPosterPath(movie.poster_path)" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>{{movie.title}}</h5>
        <!-- <p></p> -->
      </div>
    </div>
    <div class="carousel-item" data-bs-interval="2000">
      <!-- <img src="..." class="d-block w-100" alt="..."> -->
      <div class="carousel-caption d-none d-md-block">
        <h5>Second slide label</h5>
        <p>Some representative placeholder content for the second slide.</p>
      </div>
    </div>
    <div class="carousel-item">
      <!-- <img src="..." class="d-block w-100" alt="..."> -->
      <div class="carousel-caption d-none d-md-block">
        <h5>Third slide label</h5>
        <p>Some representative placeholder content for the third slide.</p>
      </div>
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#Carousel" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#Carousel" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
</template>

<script>
import bootstrap from 'bootstrap'
import { mapGetters } from 'vuex'
const Carousel = document.querySelector('#Carousel')
const carouselSettings = new bootstrap.Carousel(Carousel, {
  interval: 2000,
  wrap: false,
})


export default {
  name: 'HomeCarousel',
  // components: {

  // },
  methods: {
    fullPosterPath: function (poster_path) {
      const basePosterPath = 'https://image.tmdb.org/t/p/original'
      return (basePosterPath + poster_path)
    }
  },
  computed: {
    ...mapGetters(['latestMovies',])
  },
}
</script>

<style>

</style>