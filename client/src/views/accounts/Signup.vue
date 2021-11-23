<template>
  <div class="container">
    <div class="row g-3 text-start">
      <h1>회원가입</h1>
      <div v-if="error">
        <p v-for="(error, erroridx) in error.response.data" :key="erroridx">{{error}}</p>
      </div>
    <div class="form-floating">
      <input type="text" id="username" v-model="credentials.username" class="form-control" placeholder="examplename">
      <label for="username" class="form-label">계정 이름</label>
    </div>
    <div class="form-floating">
      <input type="password" id="password" v-model="credentials.password" class="form-control" placeholder="examplepwd">
      <label for="password" class="form-label">비밀번호</label>
    </div>
    <div class="form-floating">
      <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation" @keypress.enter="signup(credentials)" class="form-control" placeholder="examplepwd">
      <label for="passwordConfirmation" class="form-label">비밀번호 확인</label>
    </div>
  </div>
    <button @click="signup(credentials)" class="btn btn-primary btn-lg m-3">가입하기</button>
    <router-link :to="{name: 'Home'}" class="btn btn-secondary btn-lg m-3">뒤로</router-link>
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
      error: null,
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
        this.error = error
      })

    }
  }
}
</script>