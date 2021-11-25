<template>
  <div class="d-flex flex-column align-items-center">
    <SearchMoviecard v-for="(movie, idx) in search_movie_calData" :key="idx" :movie="movie" />
    <!-- <div v-for="(movie, idx) in movies" :key="idx">
      <MovieCard :movie="movie" />
    </div> -->
    <v-pagination
      class="d-flex justify-content-center"
      v-model="curPageNum"
      :page-count="search_movie_numOfPages"
      > 
    </v-pagination>
  </div>
</template>

<script>
import vPagination from '@/components/vPagination'
import SearchMoviecard from '@/components/SearchMoviecard'
export default {
  name: 'SearchList',
  components: {
    SearchMoviecard,
    vPagination,
  },
  data: function () {
    return {
      dataPerPage: 5,
      curPageNum: 1.,
    }
  },
  props: {
    movies: Array,
  },
  computed: {
    startOffset() {
      return ((this.curPageNum - 1) * this.dataPerPage);
    },
    endOffset() {
      return (this.startOffset + this.dataPerPage);
    },
    search_movie_numOfPages() {
      return Math.ceil(this.movies.length / this.dataPerPage);
    },
    search_movie_calData() {
      return this.movies.slice(this.startOffset, this.endOffset)
    },
  },
  watch: {
    movies: function () {
      this.curPageNum = 1
    }
  },
}
</script>

<style>

</style>