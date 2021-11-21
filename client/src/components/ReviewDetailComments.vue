<template>
  <div>
    <p>
    {{ comment.user.username }} <br>
    {{ comment.content }}
    </p>
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