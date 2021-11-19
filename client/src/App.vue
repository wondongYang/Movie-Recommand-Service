<template>
  <div id="app">
    <div id="nav" class="navbar navbar-light bg-light sticky-top mb-5">
      <div class="container">
        <router-link class="text-decoration-none" :to="{name: 'Home'}">
        <span class="navbar-brand me-auto">SoySource</span>
        </router-link>
        <!-- <router-link :to="{name: 'Home'}">Home</router-link> -->
        <div v-if="login">
          <router-link :to="{name: 'Recommend'}" class="ms-3">Recommendation</router-link>
          <router-link to="#" @click.native="logout" class="ms-3">Logout</router-link>
        </div>
        <div v-else>
          <router-link :to="{name: 'Login'}" class="ms-3">Login</router-link>
          <router-link :to="{name: 'Signup'}" class="ms-3">Signup</router-link>
        </div>
      </div>
    </div>
    <router-view @login="login = true" />

    <footer>
      
    </footer>

  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      login: false
    }
  },
  methods: {
    logout: function () {
      localStorage.removeItem('jwt')
      this.$store.dispatch('setLogout')
      this.login = false
    }
  },

  created: function () {
    // 영화 들고 오기
    this.$store.dispatch('getHomeMovies')

    // state로 로그인 체크
    this.login = this.$store.state.login
    
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
