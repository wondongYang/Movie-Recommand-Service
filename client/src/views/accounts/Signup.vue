<template>
  <div class="container">
    <div class="row g-3 text-start">
      <h1>회원가입</h1>
    <div>
      <label for="username" class="form-label">계정 이름</label>
      <input type="text" id="username" v-model="credentials.username" class="form-control">
    </div>
    <div>
      <label for="password" class="form-label">비밀번호</label>
      <input type="password" id="password" v-model="credentials.password" class="form-control">
    </div>
    <div>
      <label for="passwordConfirmation" class="form-label">비밀번호 확인</label>
      <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation" @keypress.enter="signup(credentials)" class="form-control">
    </div>
  </div>
    <button @click="signup(credentials)" class="btn btn-primary m-3">가입하기</button>
    <router-link :to="{name: 'Home'}" class="btn btn-secondary m-3">뒤로</router-link>
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