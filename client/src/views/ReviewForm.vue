<template>
  <div class="container">
    <div class="mb-3 text-start">
      <label for="movie" class="form-label me-auto">영화</label>
      <input id="movie" type="text" :placeholder="movie.title" class="form-control"> <br>
    </div>
    <div class="mb-3 text-start">
      <label for="rank" class="form-label me-auto">별점</label>
      <input id="rank" type="text" v-model.trim="rank" class="form-control"> <br>
    </div>
    <div class="mb-3 text-start">
      <label for="content" class="form-label">내용</label>
      <textarea id="content" v-model="content" cols="30" rows="10" class="form-control"></textarea> <br>
    </div>
    <div class="d-flex justify-content-end">
      <button class="btn btn-primary me-3" @click="createReview">작성</button>
      <!-- <router-link :to="{name: 'MovieDetail', params:{ movieId:  }}" class="btn btn-secondary" >취소</router-link> -->
      <router-link :to="{name: 'Home',}" class="btn btn-secondary" >취소</router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'ReviewForm',
  props: {
    movie: Object,
  },
  data: function () {
    return {
      content: '',
      rank: '',

    }
  },
  methods: {
    createReview: function () {
      const review = {
        title: this.title,
        content: this.content,
        rank: this.rank,
      }
      console.log(review)
      axios({
        method: 'post',
        url: `${SERVER_URL}/create/`,
        data: review,
      })
      .then(response => {
        console.log(response)
      })
      .catch(error => {
        console.log(error)
        
      })

    },
  }
}
</script>

<style>

</style>