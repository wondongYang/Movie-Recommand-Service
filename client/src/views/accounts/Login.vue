<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">Username: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">Password: </label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <button @click="login(credentials)">Login</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      },
    }
  },
  methods: {
    login: function (credentials) {
      axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/api-token-auth/`,   // token을 획득하도록 요청
        data: credentials
      })
      .then(response => {
        localStorage.setItem('jwt', response.data.token)  // 받아온 token을 localStorage에 저장
        // 이제 (signup과 token 발급을 제외한) django server 요청 시에는 token을 header에 넣어서 전달할 것 (TodoList 부분)
        this.$emit('login')   // "나 로그인했다!!!"고 상위 component에 전달
        this.$router.push({name: 'Home'})   // Home으로 이동
      })
      .catch(error => {
        console.log(error)
      })
      
    }
  }
}
</script>