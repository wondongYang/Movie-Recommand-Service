<template>
  <div class="container">
    <div v-if="review">
      <div class="d-flex justify-content-between">
        <!-- <router-link :to="{name: 'MovieDetail', params: {'movieId': review.movie.id }}" class="btn btn-secondary me-auto" >뒤로</router-link> -->
        <button @click="$router.go(-1)" class="btn btn-secondary me-auto" >뒤로</button>
        <!-- <router-link :to="router.go(-1)" class="btn btn-secondary me-auto" >뒤로</router-link> -->
        <div>좋아요 수: {{ count }}</div>
      </div>
      <div>
        <div v-if="like" class="d-flex justify-content-end">
          <button @click="LikeReview(reviewId)" class="btn btn-link">
            <i class="fa-solid fa-thumbs-down"></i>
          </button>
        </div>
        <div v-else class="d-flex justify-content-end">
          <button @click="LikeReview(reviewId)" class="btn btn-link">
            <i class="fa-solid fa-thumbs-up"></i>
          </button>
        </div>   
      </div>
      <hr>
      <div class="row">
        <div class="col-12 text-start">
          <h3>{{ review.movie.title }}</h3>
          <div>
            <span><router-link :to="{name: 'Profile', params: {'username': review.user.username}}">{{ review.user.username }}</router-link></span>
          </div>
          <div class="text-start fs-2 star">
            {{ rank_repr }}<span class="fs-6">/5</span>
          </div>
          <div>
            <br>
            <p>{{ review.content }}</p>
            <p class="text-end">{{ review.updated_at | yyyyMMdd }}</p>
          </div>
          <div v-if="username === review.user.username" class="text-end">
            <router-link :to="{name: 'UpdateReviewForm', params:{reviewId: review.id, movieId: review.movie.id}}">
              <button class="btn btn-warning m-1">수정</button>
            </router-link>
            <!-- <button class="btn btn-warning m-1" @click="deleteReview">삭제</button> -->
            <button class="btn btn-warning m-1" data-bs-toggle="modal" data-bs-target="#deleteModal">삭제</button>
              <div class="modal fade text-center" id="deleteModal" tabindex="-1" aria-labelledby="deleteModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-sm modal-dialog-centered">
                  <div class="modal-content">
                    <div class="modal-body">
                      정말 삭제하시겠습니까?
                    </div>
                    <div class="modal-footer">
                      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
                      <button type="button" class="btn btn-warning" data-bs-dismiss="modal" @click="deleteReview">삭제</button>
                    </div>
                  </div>
                </div>
              </div>
          </div>
        </div>
      <hr>
      <div v-if="review">
        <!-- 현재 django에 Review에서 Comment를 불러올 related_name이 없음 -->
        <div v-for="comment in review.comments" :key="comment.id">
          <ReviewDetailComments :comment="comment" @commentDeleted="getReview" @onClickUpdateComment="setUpdateCommentForm(comment.id)" />
          <ReviewDetailCommentsform class="visually-hidden" :reviewId="reviewId" @commentUpdated="onCommentUpdated(comment.id)" :id="'comment'+comment.id" :data-id="comment.id" :mode="'put'" :initCommentInput="comment.content" />
          <br>
        </div>
        <div v-if="login">
        <ReviewDetailCommentsform :reviewId="reviewId" @commentAdded="getReview" :mode="'post'" />
        </div>
        <div v-else>
          <router-link :to="{name: 'Login'}">댓글을 남기려면 로그인하세요.</router-link>
        </div>
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
import { mapActions, mapState } from 'vuex'
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
      like: null,
      count: null,
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
        this.count = this.review.like_users.length
        this.like = this.review.like_users.some((element) => {
          if(element === this.review.user.id) {
            return true
          }
        })
      })
      .catch(error => {
        console.log(error)
      })
    },
    LikeReview: function (reviewId) {
      const like = {
        review: Number(this.$route.params.reviewId),
        like: this.like,
      }
      this.setToken()
      axios({
        method: 'POST',
        url: `${SERVER_URL}/community/${reviewId}/likes/`,
        headers: this.$store.state.tokenStr,
        data: like,     
      })
      .then((response) => {
        console.log(this.review.like_users)
        console.log(this.review.user)
        this.like = !this.like
        this.count = response.data.count
      })
    }, 

    setUpdateCommentForm: function (commentId) {
      const picked = document.querySelector(`#comment${commentId}`)
      picked.classList.toggle('visually-hidden')
    },

    onCommentUpdated: function (commentId) {
      const picked = document.querySelector(`#comment${commentId}`)
      picked.classList.toggle('visually-hidden')
      this.getReview()
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
        this.$router.push({name: 'MovieDetail', params: {'movieId': this.review.movie.id }})
      })
      .catch(error => {
        console.log(error)
      })
    },

    // setUpdateCommentForm: function (comment) {

    // },
    ...mapActions(['setToken', ])
  },
  computed: {
    rank_repr: function () {
      let stars = ['', '★', '★★', '★★★', '★★★★', '★★★★★']
      return stars[this.review.rank]
    },
    username: function () {
      return this.$store.state.username
    },
    ...mapState(['login'])
  },
  created: function () {
    this.getReview()
  },
  filters: {
    yyyyMMdd: function (value) {
      // 현재 Date 혹은 DateTime 데이터를 javaScript date 타입화
      var js_date = new Date(value);

      var year = js_date.getFullYear();
      var month = js_date.getMonth() + 1;
      var day = js_date.getDate();
      var hour = js_date.getHours();
      var min = js_date.getMinutes();

      if(month < 10){
        month = '0' + month;
      }

      if(day < 10){
        day = '0' + day;
      }

      if(hour < 10){
        hour = '0' + hour;
      }

      if(min < 10){
        min = '0' + min;
      }

      return year + '.' + month + '.' + day + ' ' + hour + '시 ' + min + '분'; 
    }
  }
}
</script>

<style>

</style>