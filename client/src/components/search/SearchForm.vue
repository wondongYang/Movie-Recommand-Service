<template>
  <div>
    <input type="text" v-model="query" @keyup.enter="inputSearch(query)">
    <button @click="inputSearch(query)">검색</button>
  </div>
</template>

<script>
export default {
  name: 'SearchForm',
  data: function () {
    return {
      query: '',
    }
  },
  methods: {
    inputSearch: function (query) {
      console.log(query)
      this.$emit('inputSearch', query)
    },
  }
}
</script>

<style>

</style>