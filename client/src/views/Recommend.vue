<template>
  <div>
    <RecommendModel1 />
  </div>
</template>

<script>
import RecommendModel1 from '@/components/Recommend/RecommendModel1'
import { mapGetters } from 'vuex'

export default {
  name: 'Recommend',
  components: {
    RecommendModel1
  },
  data: function () {
    return {
    }
  },
  methods: {
    // getMovieDetail: function () {
      
    // },
    SelectMyGenre: function () {
      console.log(this)
    },
  },
  computed: {
    ...mapGetters(['HomeGenreMovies',])
  }
}
</script>
