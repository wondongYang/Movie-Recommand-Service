<template>
  <div class="container">
    <hr>
    <div class="text-start">
      <p>This is MovieDetailReview.</p>
      <p>{{ movieId }}(movieId)를 들고 Review 찾기</p>
    </div>

    <div class="ms-auto">
      <router-link :to="{name: 'ReviewForm'}" class="btn btn-primary ms-auto">리뷰 작성하기</router-link>
    </div>
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