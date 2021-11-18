<template>
  <div>
    <p>This is MovieDetailReview.</p>
    <p>{{ movieId }}(movieId)를 들고 Review 찾기</p>
    <router-link :to="{name: 'ReviewForm'}">리뷰 작성하기</router-link>
  </div>
</template>

<script>
export default {
  name: 'MovieDetailReview',
  props: {
    movieId: Number,
  }
}
</script>

<style>

</style>