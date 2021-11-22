<template>
  <div class="container">
    <div v-if="review">
      <div class="d-flex">
        <router-link :to="{name: 'MovieDetail', params: {movieId: review.movie.id }}" class="btn btn-secondary me-auto" >뒤로</router-link>
      </div>
      <hr>
      <div class="row">
        <div class="col-12 text-start">
          <h3>{{ review.movie.title }}</h3>
          <div>
            <span>{{ review.user.username }}</span>
          </div>
          <div class="text-start fs-2">
            {{ rank_repr }}<span class="fs-6">/5</span>
          </div>
          <div>
            <br>
            <p>{{ review.content }}</p>
            <p class="text-end">{{ review.updated_at }}</p>
          </div>
          <div v-if="username === review.user.username" class="text-end">
            <button class="btn btn-warning m-1">수정</button>
            <button class="btn btn-warning m-1" @click="deleteReview">삭제</button>
          </div>
        </div>
      <hr>
      <div v-if="review">
        <!-- 현재 django에 Review에서 Comment를 불러올 related_name이 없음 -->
        <div v-for="(comment, idx) in review.comments" :key="idx">
          <ReviewDetailComments :comment="comment" @commentDeleted="getReview" />
        </div>
        <ReviewDetailCommentsform :reviewId="reviewId" @commentAdded="getReview" />
        <!-- {{ review.comment_set }} -->
      </div>
     </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewDetailComments from '@/components/ReviewDetailComments'
import ReviewDetailCommentsform from '@/components/ReviewDetailCommentsform'
import { mapActions } from 'vuex'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewDetail',
  components: {
    ReviewDetailComments, ReviewDetailCommentsform
  },
  data: function () {
    return {
      reviewId: Number(this.$route.params.reviewId),
      review: {
        movie: {},
        user: {},
      },
    }
  },
  methods: {
    // setToken: function () {
    //   const token = localStorage.getItem('jwt')
    //   const config = {
    //     Authorization: `JWT ${token}`,
    //   }
    //   return config
    // },

    getReview: function () {
      // this.setToken()
      axios({
        method: 'get',
        // django 에서 review detail을 받아올 주소
        url: `${SERVER_URL}/community/${this.reviewId}/`,
        // headers: this.$store.state.tokenStr,
      })
      .then(response => {
        this.review = response.data
      })
      .catch(error => {
        console.log(error)
      })
    },

    deleteReview: function () {
      this.setToken()
      axios({
        method: 'delete',
        url: `${SERVER_URL}/community/${this.reviewId}/`,
        headers: this.$store.state.tokenStr,
      })
      .then(() => {
        // review를 삭제하고 나면 영화 페이지로 이동
        this.$router.push({name: 'MovieDetail', params: {movieId: this.review.movie.id }})
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
      return stars[this.review.rank]
    },
    username: function () {
      return this.$store.state.username
    },
  },
  created: function () {
    this.getReview()
  }
}
</script>

<style>

</style>