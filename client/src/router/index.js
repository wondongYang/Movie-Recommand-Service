import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home'
import Recommend from '@/views/Recommend'
import MovieDetail from '@/views/MovieDetail'
import ReviewForm from '@/views/ReviewForm'
import ReviewDetail from '@/views/ReviewDetail'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: Recommend
  },
  {
    path: '/movies/:movieId',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/movies/:movieId/reviewform',
    name: 'ReviewForm',
    component: ReviewForm
  },
  {
    path: '/movies/:movieId/:reviewId',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
