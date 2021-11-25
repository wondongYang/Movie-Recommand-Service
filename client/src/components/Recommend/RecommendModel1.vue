<template>
  <div>
    <div v-if="genre == ''">
      <p>좋아하는 영화에 좋아요와 리뷰를 남기면 <br>새 영화를 추천해드립니다!</p>
    </div>
    <div v-else>
      <p>
        <span class="fw-bold">{{ genre }}</span>
        를 좋아하는 {{ username}}님, 혹시 이 영화는 보셨나요?
      </p>
      <div class="d-flex flex-wrap justify-content-evenly p-3">
        <div v-for="(movie, idx) in movies" :key="idx">
          <MovieCard :movie="movie" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'
import MovieCard from '@/components/MovieCard'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'RecommendModel1',
  components: {
    MovieCard,
  },
  data: function () {
    return {
      genre: '',
      movies: []
    }
  },
  methods: {
    getRecommend: function () {
      this.setToken()
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/recommended/model1/`,
        headers: this.$store.state.tokenStr,
      })
      .then(response => {
        this.genre = response.data.genre.name
        this.movies = response.data.recommendations
      })
      .catch(error => {
        console.log(error)
      })
    },


    ...mapActions(['setToken',])
  },
  created: function () {
    this.getRecommend()
  },
  computed: {
    username: function () {
      return this.$store.state.username
    },
  },
}
</script>

<style>

</style>