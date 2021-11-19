<template>
  <div class="container">
    <router-link :to="{name: 'ReviewDetail', params:{reviewId: review.id}}">
      <p>{{review.content}} | {{review.rank}}점 | {{review.user}}</p>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'MovieDetailReview',
  props: {
    review: Object,
  },
}
</script>

<style>

</style>