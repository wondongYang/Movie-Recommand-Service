<template>
  <div>
    <div v-if="review">
      <div>
        리뷰를 받았습니다.
        리뷰 내용이 들어갈 공간:
        {{ review.user }}
        {{ review.rank }}
        {{ review.content }}
        {{ review.updated_at }}
      </div>
      <div>
        수정 삭제 기능:

      </div>
      <div>
        리뷰 댓글이 들어갈 공간:
        <ReviewDetailComments />
        <!-- {{ review.comment_set }} -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewDetailComments from '@/components/ReviewDetailComments'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewDetail',
  components: {
    ReviewDetailComments, 
  },
  data: function () {
    return {
      reviewId: this.$route.params.reviewId,
      review: null,
    }
  },
  methods: {
    getReview: function () {
      axios({
        method: 'get',
        // django 에서 review detail을 받아올 주소
        url: `${SERVER_URL}/community/${this.reviewId}`,
        // headers: 
      })
      .then(response => {
        console.log(response)
        this.review = response.data
      })
      .catch(error => {
        console.log(error)
      })
    },

    deleteReview: function () {
      axios({
        method: 'delete',
        url: `${SERVER_URL}/community/${this.reviewId}`,
        // headers: 
      })
      .then(response => {
        console.log(response)
        // review를 삭제하고 나면 영화 페이지로 이동
        // this.$router.push({name: 'MovieDetail', params:{ movieId: }})
        
      })
      .catch(error => {
        console.log(error)
      })
    }

  },
  created: function () {
    this.getReview()
  }
}
</script>

<style>

</style>