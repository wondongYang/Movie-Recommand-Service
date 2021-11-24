<template>
  <div class="container form-signin needs-validation">
    <div class="row g-3 text-start">
      <h1>로그인</h1>
      <div v-if="error" class="alert alert-warning">
        <p v-for="(error, erroridx) in error.response.data" :key="erroridx">{{error}}</p>
      </div>
      <div class="form-floating has-validation">
        <input type="text" id="username" v-model="credentials.username" class="floatingInput form-control" placeholder="examplename">
        <label for="username" class="form-label">계정 이름</label>
        <div class="invalid-feedback">
        Please choose a username.
        </div>
      </div>
      <div class="form-floating">
        <input type="password" id="password" v-model="credentials.password" class="form-control" @keypress.enter="login(credentials)" placeholder="examplepwd">
        <label for="password" class="form-label">비밀번호</label>
      </div>
    </div>
    <button @click="login(credentials)" class="btn btn-primary btn-lg m-3">로그인</button>
    <router-link :to="{name: 'Home'}" class="btn btn-secondary btn-lg m-3">뒤로</router-link>
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
      error: null,
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
        // this.$emit('login')   // "나 로그인했다!!!"고 상위 component에 전달
        this.$store.dispatch('setLogin', credentials.username)
        this.$router.push({name: 'Home'})   // Home으로 이동
      })
      .catch(error => {
        console.log(error)
        this.error = error
      })
      
    }
  }
}
</script>