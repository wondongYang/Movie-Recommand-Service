<template>
  <div>
    <SearchForm @inputSearch="getSearch" />
    <SearchList :movies="movies" />
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL
import axios from 'axios'
import SearchForm from '@/components/search/SearchForm'
import SearchList from '@/components/search/SearchList'
export default {
  name: 'Search',
  components: {
    SearchForm, SearchList,
  },
  data: function () {
    return {
      query: '',
      movies: [],
    }
  },
  methods: {
    getSearch: function (query) {
      console.log(query)
      this.query = query
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/search/`,
        params: {
          q: query,
          page: 1,
        },
      })
      .then(response => {
        this.movies = response.data
      })
      .catch(error => {
        console.log(error)
      })

    }
  }

}
</script>

<style>

</style>