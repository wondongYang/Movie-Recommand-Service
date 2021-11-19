<template>
  <div class="row">
    <div class="col-10">
      <input v-model="commentInput" @keypress.enter="addComment" type="text" name="content" class="form-control">
    </div>
    <div class="col-2">
      <button @click="addComment" class="btn btn-primary me-3">작성</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
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

      const comment = {
        content: this.commentInput,
      }
      axios({
        method: 'post',
        url: `${SERVER_URL}/community/${this.reviewId}/comments/create/`,
        headers: this.$store.dispatch('setToken'),
        data: comment,
      })
      .then(response => {
        console.log(response)
      })
      .catch(error => {
        console.log(error)
      })

    }
  },
}
</script>

<style>

</style>