<template>
  <div class="container">
    <router-link :to="{name: 'ReviewDetail', params:{reviewId: review.id}}" class="text-decoration-none">
      <div class="d-flex justify-content-between">
      <p>{{ review.content }}</p>
      <p>{{review.rank}} {{review.user.username}}</p>
      </div>
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