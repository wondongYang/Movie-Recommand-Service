import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home'
import Recommend from '@/views/Recommend'
import MovieDetail from '@/views/MovieDetail'
import ReviewForm from '@/views/ReviewForm'
import ReviewDetail from '@/views/ReviewDetail'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Profile from '@/views/accounts/Profile'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/accounts/:username',
    name: 'Profile',
    component: Profile
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
    path: '/community/:reviewId',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
  {
    path: '/movies/:movieId/reviewform/:reviewId',
    name: 'UpdateReviewForm',
    component: ReviewForm
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
