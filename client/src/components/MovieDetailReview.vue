<template>
  <div class="container">
    <router-link :to="{name: 'ReviewDetail', params:{reviewId: review.id}}" class="text-decoration-none">
      <div class="d-flex justify-content-between">
      <p>{{ review.content }}</p>
      <p>{{ rank_repr }} {{review.user.username}}</p>
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
    }
  }
}
</script>

<style>

</style>