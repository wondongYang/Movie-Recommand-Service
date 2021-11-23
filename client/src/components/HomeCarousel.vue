<template>
  <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-indicators">
      <!-- 시작부분만 active를 설정 -->
      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
      <button v-for="(movie, idx) in latestMovies" :key="idx"
      type="button" data-bs-target="#carouselExampleIndicators" :data-bs-slide-to="idx+1" :aria-label="`Slide ${idx+1}`"
      aria-current="true"></button>
    </div>
    <div class="carousel-inner">
      <!-- 시작부분만 active를 설정 -->
      <div class="carousel-item active">
        <img :src="firstMoviePosterPath(latestMovies[0])" class="d-block w-100" alt="...">
      </div>
      <div v-for="(movie, idx) in latestMovies.slice(1)" :key="idx"
      class="carousel-item">
        <img :src="fullPosterPath(movie.poster_path)" class="d-block w-100" alt="...">            
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
    <h3>최근 개봉작</h3>
    <!-- 영화 목록 16개를 2차원 배열로 받아옴 -->
    <button @click="makeMovieBoxList(latestMovies)">123123</button>
    <!-- <div v-if="latestMovies" class="d-flex flex-wrap justify-content-evenly p-3">
      <MovieCard v-for="(movie, idx) in latestMovies" :key="idx" :movie="movie" />
    </div>
    <div v-for="(MovieBox, idx) in MovieBoxList" :key="idx" :MovieBox="MovieBox" class="d-flex flex-wrap justify-content-evenly p-3">
      <MovieCard v-for="(movie, idx) in MovieBox" :key="idx" :movie="movie" />
    </div> -->
    <hr><hr><hr>
  </div>
</template>

<script>
// import MovieCard from '@/components/MovieCard'
// import bootstrap from 'bootstrap'
import { mapGetters } from 'vuex'
// const Carousel = document.querySelector('#Carousel')
// const carouselSettings = new bootstrap.Carousel(Carousel, {
//   interval: 2000,
//   wrap: false,
// })


export default {
  name: 'HomeCarousel',
  components: {
    // MovieCard,
  },
  data: function () {
    return {
      MovieBoxList: [],
    }
  },
  methods: {
    makeMovieBoxList: function (movies) {
      for(var i=0; i<4; i++){
        this.MovieBoxList[i] = [];
        for(var j=0; j<4; j++){
          this.MovieBoxList[i][j] = null;
        }
      }
      var num = 0;
      for(var k=0; k<4; k++){
        for(var t=0; t<4; t++){
          this.MovieBoxList[k][t] = movies[num]
          num = num+1
        }
      }
      console.log(this.MovieBoxList)
    },
    firstMoviePosterPath: function (movie) {
      const basePosterPath = 'https://image.tmdb.org/t/p/original'
      return (basePosterPath + movie.poster_path)
    },
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