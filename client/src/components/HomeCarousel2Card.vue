<template>
  <div class="card bg-dark text-white mb-3" style="max-width: 1440px;">
    <router-link :to="{name: 'MovieDetail', params: {movieId: movie.id}}" :movie="movie" class="text-decoration-none link-light">
    <div class="row g-0">
      <div class="col-md-4">
        <img :src="fullPosterPath" class="img-fluid rounded-start" alt="movie poster">
      </div>
      <div class="col-md-8">
        <div class="card-body text-start m-3">
          <h5 class="card-title">{{ movie.title }}</h5>
          <p class="card-text"><small class="text-muted"><span v-for="(genre, id) in movie.genre_ids" :key="id">#{{genre.name}} </span></small></p>
          <br>
          <p class="card-text">{{ movie.overview | overviewAbbr }}</p>
          <p class="card-text text-end"><small class="text-muted"><span class="text-danger">❤</span> {{ movie.like_users.length }} | 📝 {{ movie.reviews.length }}</small></p>
          <!-- 리뷰를 넣는 칸 -->
          <p class="card-text">{{ Review1(movie) | reviewAbbr }}</p>
          <p class="card-text">{{ Review2(movie) | reviewAbbr  }}</p>
          <p class="card-text">{{ Review3(movie) | reviewAbbr  }}</p>
          <p class="card-text">{{ Review4(movie) | reviewAbbr  }}</p>
          <p class="card-text">{{ Review5(movie) | reviewAbbr  }}</p>
        </div>
      </div>
    </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'HomeCarousel2Card',
  props: {
    movie: Object,
  },
  computed: {
    fullPosterPath: function () {
      const basePosterPath = 'https://image.tmdb.org/t/p/original'
      console.log(this.movie)
      return (basePosterPath + this.movie.poster_path)
    }
  },
  methods: {
    Review1: function (movie) {
      if (movie.reviews.length > 0) {
        const review = movie.reviews[0]
        const rank = review.rank
        const content = review.content
        return `${rank}점 | ${content}`
      }
      else {
        return `리뷰가 없습니다.`
      }
    },
    Review2: function (movie) {
      if (movie.reviews.length > 1) {
        const review = movie.reviews[1]
        const rank = review.rank
        const content = review.content
        return `${rank}점 | ${content}`
      }
      else {
        return ''
      }
    },
    Review3: function (movie) {
      if (movie.reviews.length > 2) {
        const review = movie.reviews[2]
        const rank = review.rank
        const content = review.content
        return `${rank}점 | ${content}`
      }
      else {
        return ''
      }
    },
    Review4: function (movie) {
      if (movie.reviews.length > 3) {
        const review = movie.reviews[3]
        const rank = review.rank
        const content = review.content
        return `${rank}점 | ${content}`
      }
      else {
        return ''
      }
    },Review5: function (movie) {
      if (movie.reviews.length > 4) {
        const review = movie.reviews[4]
        const rank = review.rank
        const content = review.content
        return `${rank}점 | ${content}`
      }
      else {
        return ''
      }
    }
  },
  filters: {
    // releaseDateRepr: function (datestring) {
    //   // YYYY-MM-DD >> YYYY년 M월 D일
    //   let [year, month, day] = datestring.split('-')
    //   month = parseInt(month)
    //   day = parseInt(day)
    //   return `${year}년 ${month}월 ${day}일`
    // },
    overviewAbbr: function (content) {
      return (content.length < 80 ? content : content.slice(0, 80) + ' ...')
    },
    reviewAbbr: function (content) {
      return (content.length < 20 ? content : content.slice(0, 20) + ' ...')
    },
  },
}
</script>

<style>

</style>