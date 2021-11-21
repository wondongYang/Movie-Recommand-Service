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
      <button class="btn btn-primary me-3" @click="createReview">작성</button>
      <router-link :to="{name: 'MovieDetail', params:{ movieId: this.$route.params.movieId }}" class="btn btn-secondary" >취소</router-link>
      <!-- <router-link :to="{name: 'Home',}" class="btn btn-secondary" >취소</router-link> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'ReviewForm',
  data: function () {
    return {
      // movie: null,
      title: '',
      content: '',
      rank: 3,
      movie: '',
    }
  },
  // props: {
  //   movie: Object,
  // },

  methods: {
    // 왜 setToken을 store에서 쓰면 Promise 객체로 나오는 걸까?
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`,
      }
      return config
    },

    createReview: function () {
      const review = {
        movie: this.$route.params.movieId,
        content: this.content,
        rank: this.rank,
      }
      axios({
        method: 'post',
        url: `${SERVER_URL}/community/create/`,
        // headers: this.$store.dispatch('setToken'),
        headers: this.setToken(),
        data: review,
      })
      .then(() => {
        this.$router.push({name: 'MovieDetail', params: {'movieId': this.$route.params.movieId}})
      })
      .catch(error => {
        console.log(error)
        
      })
    },
  },

  computed: {
    rank_repr: function () {
      let stars = ['', '★', '★★', '★★★', '★★★★', '★★★★★']
      return stars[this.rank]
    }
  },

  created: function () {
    this.movie = this.$store.state.selectedMovie
  }
}
</script>

<style>

</style>