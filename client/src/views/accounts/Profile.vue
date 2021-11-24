<template>
  <div class="container text-start">
    <div class="row g-3">
      <div class="col-md-12 col-8">
          <h1 v-if="(person.username == username)">{{ person.username }}님, 안녕하세요!</h1>
          <h1 v-else>{{ person.username }}님의 프로필입니다.</h1>
        <div>
          <p>
            가입일: {{ person.date_joined }} <br>
            <br>
          </p>
        </div>
        <div>
          <p>좋아하는 영화</p>
          <div class="d-flex flex-wrap">
            <div v-for="(movie, movieIdx) in like_movie_calData" :key="'like_movies_'+movieIdx">
              <router-link :to="{name: 'MovieDetail', params:{movieId: movie.id}}">
              <MovieSmallcard :movie="movie" />
              </router-link>
            </div>
          </div>
          <v-pagination
            class="d-flex justify-content-center"
            v-model="curPageNum"
            :page-count="like_movie_numOfPages"> 
          </v-pagination>
          <p>좋아하는 리뷰</p>
          <table class="table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">영화 제목</th>
                <th scope="col">별점</th>
                <th scope="col">리뷰</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(like_review, like_reviewIdx) in like_review_calData" :key="'like_reviews_'+like_reviewIdx">
                <th scope="row">{{like_review.id}}</th>
                <td>{{like_review.movie.title}}</td>
                <td class="star">{{like_review.rank|rankRepr}}</td>
                <td>
                <router-link :to="{name: 'ReviewDetail', params:{reviewId: like_review.id}}">
                {{like_review.content|contentAbbr}}
                </router-link>
                </td>
              </tr>
            </tbody>
          </table>
          <v-pagination
            class="d-flex justify-content-center"
            v-model="curPageNum"
            :page-count="like_review_numOfPages"> 
          </v-pagination>

<!-- 
          <div v-for="(like_review, like_reviewIdx) in person.like_reviews" :key="'like_reviews_'+like_reviewIdx">
            <p>{{like_review.movie}} {{like_review.rank|rankRepr}} "{{like_review.content|contentAbbr}}" </p>
          </div> -->
        </div>
        <div>
          <p>작성 리뷰</p>
          <table class="table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">영화 제목</th>
                <th scope="col">별점</th>
                <th scope="col">리뷰</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(review, reviewIdx) in write_review_calData" :key="'review_'+reviewIdx">
                <th scope="row">{{review.id}}</th>
                <td>{{review.movie.title}}</td>
                <td class="star">{{review.rank|rankRepr}}</td>
                <td>
                <router-link :to="{name: 'ReviewDetail', params:{reviewId: review.id}}" class="text-decoration-none">
                {{review.content|contentAbbr}}
                </router-link>
                </td>
              </tr>
            </tbody>
          </table>
          <v-pagination
            class="d-flex justify-content-center"
            v-model="curPageNum"
            :page-count="write_review_numOfPages"> 
          </v-pagination>
          <br>
          <p>작성 댓글</p>
          <table class="table">
            <thead>
              <tr>
                <th scope="col">내용</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(comment, commentIdx) in write_comment_calData" :key="'comment_'+commentIdx">
                <td>{{comment.content}}</td>
              </tr>
            </tbody>
          </table>
          <v-pagination
            class="d-flex justify-content-center"
            v-model="curPageNum"
            :page-count="write_comment_numOfPages"> 
          </v-pagination>

          <!-- <div v-for="(comment, commentIdx) in person.comment_set" :key="'comment_'+commentIdx">
            <p>{{comment.content}}</p>
          </div> -->
        </div>
      </div>
      <div class="col-md-4 col-12 text-end">
        <!-- <button></button>
        <br>
        <button>회원정보 수정</button> -->
      </div>
    </div>
  </div>
</template>

<script>
import vPagination from '@/components/vPagination'
import axios from 'axios'
import MovieSmallcard from '@/components/MovieSmallcard'
import { mapState } from 'vuex'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'Profile',
  components: {
    MovieSmallcard,
    vPagination,
  },
  data: function () {
    return {
      person: {},
      dataPerPage: 5,
      curPageNum: 1,
    }
  },
  methods: {
    getUserInfo: function (username) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/accounts/profile/${username}/`,
      })
      .then(response => {
        this.person = response.data
        console.log(this.person)
      })
      .catch(error => {
        console.log(error)
      })
    },
  },
  computed: {
    ...mapState(['username']),
    startOffset() {
      return ((this.curPageNum - 1) * this.dataPerPage);
    },
    endOffset() {
      return (this.startOffset + this.dataPerPage);
    },
    // 좋아하는 영화 pagination
    like_movie_numOfPages() {
      return Math.ceil(this.person.like_movies.length / this.dataPerPage);
    },
    like_movie_calData() {
      return this.person.like_movies.slice(this.startOffset, this.endOffset)
    },
    // 좋아하는 리뷰 pagination
    like_review_numOfPages() {
      return Math.ceil(this.person.like_reviews.length / this.dataPerPage);
    },
    like_review_calData() {
      return this.person.like_reviews.slice(this.startOffset, this.endOffset)
    },
    // 작성 리뷰 pagination
    write_review_numOfPages() {
      return Math.ceil(this.person.review_set.length / this.dataPerPage);
    },
    write_review_calData() {
      return this.person.review_set.slice(this.startOffset, this.endOffset)
    },
    // 작성 댓글 pagination
    write_comment_numOfPages() {
      return Math.ceil(this.person.comment_set.length / this.dataPerPage);
    },
    write_comment_calData() {
      return this.person.comment_set.slice(this.startOffset, this.endOffset)
    }
  },
  mounted: function () {
    this.getUserInfo(this.$route.params.username)
  },
  filters: {
    rankRepr: function (rank) {
      let stars = ['-', '★', '★★', '★★★', '★★★★', '★★★★★']
      return stars[rank]
    },
    contentAbbr: function (content) {
      return (content.length < 20 ? content : content.slice(0, 20) + ' ...')
    },
  },
}
</script>

<style> 

</style>
