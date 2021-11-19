<template>
  <div class="container">
    <hr>
    <div class="text-start">
      <p>This is MovieDetailReview.</p>
      <p>{{ movieId }}(movieId)를 들고 Review 찾기</p>
    </div>

    <div class="ms-auto">
      <router-link :to="{name: 'ReviewForm'}" class="btn btn-primary ms-auto">리뷰 작성하기</router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'MovieDetailReview',
  props: {
    movieId: Number,
  },
  created: function () {
    axios({
      method: 'get',
      url: `${SERVER_URL}/community/${reviewId}`,
    })

  }
}
</script>

<style>

</style>