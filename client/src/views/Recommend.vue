<template>
  <div>
    <p>This is Recommend.</p>
    <div class="container">
      <h2>보고 싶은 장르 선택하기</h2>
      <!-- <button @click="SelectMyGenre">{{  }}</button> -->
    </div>

    
    <div v-if="HomeGenreMovies.animation" class="d-flex flex-wrap justify-content-evenly p-3">
      <MovieCard v-for="(movie, idx) in HomeGenreMovies.animation" :key="idx" :movie="movie" />
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import { mapGetters } from 'vuex'

export default {
  name: 'Recommend',
  components: {
    MovieCard,
  },
  methods: {
    // getMovieDetail: function () {
      
    // },
    SelectMyGenre: function () {
      console.log(this)
    },
  },
  computed: {
    ...mapGetters(['HomeGenreMovies',])
  }
}
</script>
