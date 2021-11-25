<template>
  <div class="text-start">
    {{ comment.user.username }} |
    작성시간: {{ comment.created_at | yyyyMMdd }} |
    수정시간: {{ comment.updated_at | yyyyMMdd }} <br>
    {{ comment.content }}
    <span class="ms-auto" v-if="username === comment.user.username">
    <button @click="clickUpdateComment" class="btn btn-light btn-sm">수정</button>
    <button @click="deleteComment" class="btn btn-light btn-sm">삭제</button>
    </span>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'ReviewDetailComments',
  props: {
    comment: Object,
  },
  data: function () {
    return {
      reviewId: this.$route.params.reviewId
    }
  },
  methods: {
    deleteComment: function () {
      this.setToken()
      axios({
        method: 'delete',
        url: `${SERVER_URL}/community/${this.reviewId}/comments/${this.comment.id}/`,
        headers: this.$store.state.tokenStr,
      })
      .then(() => {
        // Comment 삭제 후 reload >> ReviewDetail로
        this.$emit('commentDeleted')
      })
      .catch(error => {
        console.log(error)
      })
    },
    clickUpdateComment: function () {
      this.$emit('onClickUpdateComment')
    },
    
    ...mapActions(['setToken',])
  },
  computed: {
    username: function () {
      return this.$store.state.username
    },
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