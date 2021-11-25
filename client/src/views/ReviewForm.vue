<template>
  <div class="container">
    <p>{{movie}}</p>

    <div class="mb-3 text-start">
      <label for="movie" class="form-label me-auto">영화</label>
      <input id="movie" type="text" :placeholder="$route.query.movieTitle" class="form-control" disabled> <br>
    </div>
    <div class="mb-3 text-start">
      <label for="rank" class="form-label">별점</label>
      <p>{{rank_repr}}</p>
      <input type="range" v-model="rank" class="form-range" min="1" max="5" id="rank"> 
      <!-- <label for="rank" class="form-label me-auto">별점</label>
      <input id="rank" type="text" v-model.trim="rank" class="form-control"> <br> -->
    </div>
    <div class="mb-3 text-start">
      <label for="content" class="form-label">내용</label>
      <textarea id="content" v-model="content" cols="30" rows="10" class="form-control"></textarea> <br>
    </div>
    <div class="d-flex justify-content-end">
      <button v-if="isUpdate" class="btn btn-primary me-3" @click="updateReview">수정</button>
      <button v-else class="btn btn-primary me-3" @click="createReview">작성</button>
      <button @click="$router.go(-1)" class="btn btn-secondary">취소</button>
      <!-- <router-link :to="{name: 'MovieDetail', params:{ movieId: this.$route.params.movieId }}" class="btn btn-secondary" >취소</router-link> -->
      <!-- <router-link :to="{name: 'Home',}" class="btn btn-secondary" >취소</router-link> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'ReviewForm',
  data: function () {
    return {
      // movie: null,
      content: '',
      rank: 3,
      movie: '',
      isUpdate: !!this.$route.params.reviewId,
      reviewId: this.$route.params.reviewId,
    }
  },
  // props: {
  //   movie: Object,
  // },

  methods: {
    createReview: function () {
      const review = {
        movie: this.$route.params.movieId,
        content: this.content,
        rank: this.rank,
      }
      this.setToken()
      axios({
        method: 'post',
        url: `${SERVER_URL}/community/create/`,
        headers: this.$store.state.tokenStr,
        // headers: this.setToken(),
        data: review,
      })
      .then(() => {
        this.$router.push({name: 'MovieDetail', params: {'movieId': this.$route.params.movieId}})
      })
      .catch(error => {
        console.log(error)
      })
    },
    updateReview: function () {
      const review = {
        movie: this.$route.params.movieId,
        content: this.content,
        rank: this.rank,
      }
      this.setToken()
      axios({
        method: 'put',
        url: `${SERVER_URL}/community/${this.$route.params.reviewId}/`,
        headers: this.$store.state.tokenStr,
        // headers: this.setToken(),
        data: review,
      })
      .then(() => {
        this.$router.push({name: 'MovieDetail', params: {'movieId': this.$route.params.movieId}})
      })
      .catch(error => {
        console.log(error)
      })
    },

    ...mapActions(['setToken',])
  },

  computed: {
    rank_repr: function () {
      let stars = ['', '★', '★★', '★★★', '★★★★', '★★★★★']
      return stars[this.rank]
    }
  },

  created: function () {
    this.movie = this.$store.state.selectedMovie
    if (this.isUpdate) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/community/${this.$route.params.reviewId}/`,
      })
      .then(response => {
        this.content = response.data.content
        this.rank = response.data.rank
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style>

</style>