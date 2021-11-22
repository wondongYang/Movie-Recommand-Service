<template>
  <div class="container">
    <div>
      <h1>{{ user.username }}님, 안녕하세요!</h1>
    </div>
    <div>
      <p>
        가입일: {{ user.date_joined }} <br>
        <br>
        {{ user }}
      
      </p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'Profile',
  data: function () {
    return {
      user: {}
    }
  },
  methods: {
    getUserInfo: function (username) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/accounts/profile/${username}/`,
      })
      .then(response => {
        this.user = response.data
      })
      .catch(error => {
        console.log(error)
      })
    },

  },
  created: function () {
    this.getUserInfo(this.$route.params.username)
  },
}
</script>

<style>

</style>