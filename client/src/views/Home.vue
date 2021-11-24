<template>
  <div class="home">
    <div>
      <p> 메인 화면이 들어갈 공간입니다. (Carousel이나 Wallpaper 등...)</p>
      <p> Soy Source </p>
    </div>
    <div>
      <!-- <HomeCarousel /> -->
      <HomeCarousel2 :movies="latestMovies" />
    </div>
    <br>
    <div>
      <!-- <h3>최근 개봉작</h3>
      <div v-if="latestMovies" class="d-flex flex-wrap justify-content-evenly p-3">
        <MovieCard v-for="(movie, idx) in latestMovies" :key="idx" :movie="movie" />
      </div>
      <hr> -->
      <h3>좋아요를 많이 받은 영화</h3>
      <div v-if="largestReviewMovies" class="d-flex flex-wrap justify-content-evenly p-3">
        <MovieCard v-for="(movie, idx) in largestReviewMovies" :key="idx" :movie="movie" />
      </div>
      <hr>

      <div class="container">
        <h2>장르별 영화</h2>
        <div>
          <h3 class="text-start">액션</h3>
          <div v-if="HomeGenreMovies.action" class="d-flex flex-wrap justify-content-evenly p-3">
            <MovieCard v-for="(movie, idx) in HomeGenreMovies.action" :key="idx" :movie="movie" />
          </div>
        </div>
        <div>
          <h3 class="text-start">드라마</h3>
          <div v-if="HomeGenreMovies.drama" class="d-flex flex-wrap justify-content-evenly p-3">
            <MovieCard v-for="(movie, idx) in HomeGenreMovies.drama" :key="idx" :movie="movie" />
          </div>
        </div>
        <div>
          <h3 class="text-start">애니메이션</h3>
          <div v-if="HomeGenreMovies.animation" class="d-flex flex-wrap justify-content-evenly p-3">
            <MovieCard v-for="(movie, idx) in HomeGenreMovies.animation" :key="idx" :movie="movie" />
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
// @ is an alias to /src
// import {mapActions} from 'vuex'
import MovieCard from '@/components/MovieCard'
// import HomeCarousel from '@/components/HomeCarousel'
import HomeCarousel2 from '@/components/HomeCarousel2'
import { mapGetters } from 'vuex'
export default {
  name: 'Home',
  components: {
    MovieCard,
    // HomeCarousel,
    HomeCarousel2,
  },
  computed: {
    ...mapGetters(['latestMovies','largestReviewMovies','HomeGenreMovies',])
  },
}
</script>
