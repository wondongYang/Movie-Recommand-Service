<template>
  <div class="d-flex flex-row-reverse align-items-center">
    <div class="m-3">
      <button @click="addComment" class="btn btn-primary">작성</button>
    </div>
    <div class="flex-grow-1">
      <input v-model="commentInput" @keypress.enter="addComment" type="text" name="content" class="form-control" >
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewDetailCommentsform',
  props: {
    reviewId: Number,
  },
  data: function () {
    return {
      commentInput: ''
    }
  },
  methods: {
    addComment: function () {
      if (this.commentInput != '') {
        const comment = {
          content: this.commentInput,
        }
        this.setToken()
        axios({
          method: 'post',
          url: `${SERVER_URL}/community/${this.reviewId}/comments/create/`,
          // headers: this.setToken(),
          headers: this.$store.state.tokenStr,
          data: comment,
        })
        .then(() => {
          this.$emit('commentAdded')
          this.commentInput = ''
        })
        .catch(error => {
          console.log(error)
        })
      }
    },
    ...mapActions(['setToken',])
  },
}
</script>

<style>

</style>