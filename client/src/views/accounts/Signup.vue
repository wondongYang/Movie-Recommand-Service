<template>
  <div>
    <h1>Sign Up</h1>
    <div>
      <label for="username">Username: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">Password: </label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <div>
      <label for="passwordConfirmation">Confirm Password: </label>
      <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation" @keypress.enter="signup(credentials)">
    </div>
    <button @click="signup(credentials)">Sign Up</button>
  </div>
</template>

<script>
import axios from 'axios'

// 환경변수
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      },
    }
  },
  methods: {
    signup: function (credentials) {
      axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/signup/`,
        data: credentials,
      })
      .then(() => {
        this.$router.push({name: 'Login'})
      })
      .catch(error => {
        console.log(error)
      })

    }
  }
}
</script>