import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUser, faEnvelope,faLock } from '@fortawesome/free-solid-svg-icons'
import {faFacebook,faGoogle,faTwitter } from '@fortawesome/fontawesome-free-brands'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

Vue.config.productionTip = false


library.add(faUser, faFacebook,faGoogle,faLock,faTwitter,faEnvelope)
Vue.component('font-awesome-icons', FontAwesomeIcon)
new Vue({
  vuetify,
  router,
  render: h => h(App)
})
.$mount('#app')
