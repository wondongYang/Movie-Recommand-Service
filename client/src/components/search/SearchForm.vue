<template>
  <div class="d-flex flex-row-reverse align-items-center">
    <div class="m-3">
      <button @click="inputSearch(query)" class="btn btn-primary">검색</button>
    </div>
    <div class="flex-grow-1 m-3">
      <input type="text" v-model="query" @keyup.enter="inputSearch(query)" class="form-control">
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'SearchForm',
  data: function () {
    return {
      query: '',
    }
  },
  methods: {
    inputSearch: function (query) {
      console.log('wow')
      if (_.trim(query)) {
        console.log(query)
        this.$emit('inputSearch', query)
      }
    },
  }
}
</script>

<style>

</style>