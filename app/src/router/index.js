import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
//import DevicesView from '../views/DevicesView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import ServerView from '../views/ServerView.vue'
import AddDeviceView from '../views/AddDeviceView.vue'
import ControlsView from '../views/ControlsView.vue'
import UtilsView from "@/views/UtilsView.vue";
import util from '@/util'
import store from '@/store'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/devices',
    name: 'devices',
    component: AddDeviceView,
    meta: {requiresAuth: true}
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView
  },
  {
    path: '/server',
    name: 'server',
    component: ServerView,
    meta: { keepAlive: true, requiresAuth: true },
  },
  {
    path: '/controls/:data',
    name: 'controls',
    component: ControlsView,
    props: true,
    meta: {requiresAuth: true}
  },
  {
    path: '/utils',
    name: 'utils',
    component: UtilsView,
    meta: {requiresAuth: true}
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(async (to, from, next) => {
  if(to.meta.requiresAuth) {
    const validToken = util.checkToken(store.state.accessToken)
    if(validToken) {
      console.log('Token is valid')
      next()
    }
    else {
      next({ name: 'login'})
    }
  }
  else {
    next()
  }
})
export default router
