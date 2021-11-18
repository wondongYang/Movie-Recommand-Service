<template>
  <div id="app">
    <div id="nav" class="navbar navbar-light bg-light sticky-top mb-5">
      <div class="container">
        <span class="navbar-brand me-auto">SPA Movie App</span>
        <router-link :to="{name: 'Home'}">Home</router-link>
        <router-link :to="{name: 'Recommend'}" class="ms-3">Recommendation</router-link>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  created: function () {
    this.$store.dispatch('getHomeMovies')
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
