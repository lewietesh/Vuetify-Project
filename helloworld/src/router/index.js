import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomeView.vue')
  },
  {
    path: '/login',
    name: 'login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/LoginView.vue')
  },
  {
    path: '/article/:id',
    name: 'article',
    component: () => import('../views/SingleBlogView.vue')
  },
  {
    path:'/manage',
    name: 'manage',
    component: () => import('../views/ManageView.vue'),
    beforeEach: () => {

    }
  },
  {
    path:'/setting',
    name: 'setting',
    component: () => import('../views/SettingView.vue'),
    beforeEach: () => {

    }
  },
  {
    path: '*',
    name: 'pagenotfound',
    component: () => import('../views/404View.vue')
  }

]

const router = new VueRouter({
  routes,
  mode:'history'
})

export default router
