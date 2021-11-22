<template>
  <div class="text-start">
    {{ comment.user.username }} <br>
    {{ comment.content }}
    <span class="ms-auto" >
    <button v-if="username === comment.user.username" @click="deleteComment" class="btn btn-light btn-sm">❌</button>
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
    ...mapActions(['setToken',])
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