import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/label',
    name: 'label',
    component: function () {
      return import(/* webpackChunkName: "label" */ '@/views/label/LabelView.vue')
    }
  },
  {
    path: '/labelform',
    name: 'labelform',
    component: function () {
      return import(/* webpackChunkName: "noteform" */ '@/views/label/LabelFormView.vue')
    }
  },
  {
    path: '/note',
    name: 'note',
    component: function () {
      return import(/* webpackChunkName: "note" */ '@/views/note/NoteView.vue')
    }
  },
  {
    path: '/noteform',
    name: 'noteform',
    component: function () {
      return import(/* webpackChunkName: "noteform" */ '@/views/note/NoteFormView.vue')
    }
  },
  {
    path: '/user',
    name: 'user',
    component: function () {
      return import(/* webpackChunkName: "user" */ '@/views/user/UserView.vue')
    }
  },
  {
    path: '/userform',
    name: 'userform',
    component: function () {
      return import(/* webpackChunkName: "userform" */ '../views/user/UserFromView.vue')
    }
  },
  {
    path: '/login',
    name: 'login',
    component: function () {
      return import(/* webpackChunkName: "login" */ '../views/user/LoginView.vue')
    }
  },
  {
    path: '/note_user',
    name: 'noteUser',
    component: function () {
      return import(/* webpackChunkName: "noteUser" */ '../views/user/NoteUserView.vue')
    }
  },
  {
    path: '*',
    component: () => import('@/views/error/NotFound.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
