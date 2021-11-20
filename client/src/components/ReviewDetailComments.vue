<template>
  <div>
    {{ comment.user.username }} : {{ comment.content }}
  </div>
</template>

<script>
export default {
  name: 'ReviewDetailComments',
  props: {
    comment: Object,
  }
}
</script>

<style>

</style>