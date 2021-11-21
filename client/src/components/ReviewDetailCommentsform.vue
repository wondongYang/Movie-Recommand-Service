<template>
  <div class="row row-cols-lg-auto g-3 align-items-center">
    <div class="col-12">
      <input v-model="commentInput" @keypress.enter="addComment" type="text" name="content" class="form-control">
      <button @click="addComment" class="btn btn-primary">작성</button>
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
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`,
      }
      return config
    },

    addComment: function () {

      if (this.commentInput != '') {
        const comment = {
          content: this.commentInput,
        }
        axios({
          method: 'post',
          url: `${SERVER_URL}/community/${this.reviewId}/comments/create/`,
          headers: this.setToken(),
          // headers: this.$store.dispatch('setToken'),
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
    }
  },
}
</script>

<style>

</style>