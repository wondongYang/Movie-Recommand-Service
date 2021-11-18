<template>
  <div>
    <label for="title">제목</label>
    <input id="title" type="text" v-model.trim="title"> <br>
    <textarea v-model="content" cols="30" rows="10"></textarea> <br>
    <button>작성</button>
    <button>취소</button>
  </div>
</template>

<script>
export default {
  name: 'ReviewForm',
  data: function () {
    return {
      title: '',
      content: ''

    }
  },

}
</script>

<style>

</style>