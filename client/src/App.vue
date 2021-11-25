<template>
  <div id="app">

    <div id="nav" class="navbar navbar-expand-lg navbar-light bg-light sticky-top">
      <div class="container-fluid">
        <router-link class="navbar-brand me-auto text-decoration-none" :to="{name: 'Home'}">
        <img src="./assets/5760.jpg" alt="" width="20" height="20" class="d-inline-block align-text-top">
        <span class="">SoySource</span>
        </router-link>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarToggler" aria-controls="navbarToggler" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div v-if="login" class="collapse navbar-collapse justify-content-end" id="navbarToggler">
            <br>
            <ul class="navbar-nav mb-2 mb-lg-0 mx-lg-5 text-end">
              <router-link :to="{name: 'Profile', params:{username: username}}" class="my-2 ms-3 nav-item" >{{ username }}</router-link>
              <router-link :to="{name: 'Recommend'}" class="my-2 ms-3 nav-item">Recommendation</router-link>
              <router-link :to="{name: 'Search'}" class="my-2 ms-3 nav-item">Search</router-link>
              <router-link to="#" @click.native="logout" class="my-2 ms-3 nav-item">Logout</router-link>
            </ul>
          </div>
          <div v-else class="collapse navbar-collapse justify-content-end" id="navbarToggler">
            <br>
            <ul class="navbar-nav mb-2 mb-lg-0 mx-lg-5 text-end">
              <router-link :to="{name: 'Login'}" class="ms-3 my-2 nav-item">Login</router-link>
              <router-link :to="{name: 'Signup'}" class="ms-3 my-2 nav-item">Signup</router-link>
              <router-link :to="{name: 'Search'}" class="ms-3 my-2 nav-item">Search</router-link>
            </ul>
          </div>
        
      </div>
    </div>
    <router-view />

  <footer class="py-3 my-4">
    <ul class="nav justify-content-center border-bottom pb-3 mb-3">
      <li class="nav-item"><a href="https://www.themoviedb.org/ " class="nav-link px-2 text-muted">Powered by TMDB</a></li>
    </ul>
    <p class="text-center text-muted">SoySource</p>
  </footer>

  </div>
</template>

<script>
import jwt from 'jsonwebtoken'
const DJANGO_SKEY = process.env.VUE_APP_DJANGO_SKEY
export default {
  name: 'App',
  data: function () {
    return {
    }
  },
  methods: {
    logout: function () {
      localStorage.removeItem('jwt')
      this.$store.dispatch('setLogout')
      this.$router.push({name: 'Home'})
    }
  },
  computed: {
    login: function () {
      return this.$store.state.login
    },
    username: function () {
      return this.$store.state.username
    }
  },
  created: function () {
    // 로그인 체크
    const token = localStorage.getItem('jwt')
    if (token) {
      const userinfo = jwt.verify(token, String(DJANGO_SKEY))
      this.$store.dispatch('setLogin', userinfo.username)
    }

    // 영화 들고 오기
    // (App 대신 Home이 로드될 때 들고 오는 것으로 수정했습니다.)

    // 필요한 장르는 일단 여기다 집어넣으시면 됩니다. (Home 부분도 연동되게 하면 좋을듯...!)
    let homeGenres = ['action', 'drama', 'animation']
    for (let genre of homeGenres) {
      this.$store.dispatch('getGenreMovies', genre)
    }
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

.star {
    color: orange;
  }

.box-shade {
  box-shadow: 0px 4px 5px 0px;
}

.wb-keep-all {
  word-break: keep-all;
}
</style>
