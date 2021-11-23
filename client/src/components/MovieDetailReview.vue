<template>
  <div class="container">
    <router-link :to="{name: 'ReviewDetail', params:{reviewId: review.id}}" class="text-decoration-none link-dark">
      <div class="d-flex justify-content-between">
      <p>{{ review.content }}</p>
      <p><span class="star">{{ rank_repr }}</span> {{review.user.username}}</p>
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
  computed: {
    rank_repr: function () {
      let stars = ['', '★', '★★', '★★★', '★★★★', '★★★★★']
      return stars[this.review.rank]
    },
  },
}
</script>

<style>
  
</style>