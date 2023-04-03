import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VueToasted from 'vue-toasted'
import VueSwal from 'vue-swal'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueToasted, {
  position: 'top-right',
  duration: 2000
})

Vue.use(VueSwal)

new Vue({
  router,
  render: function (h) { return h(App) }
}).$mount('#app')

