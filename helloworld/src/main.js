import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUser, faEnvelope,faLock } from '@fortawesome/free-solid-svg-icons'
import {faFacebook,faGoogle,faTwitter } from '@fortawesome/fontawesome-free-brands'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { ValidationObserver, ValidationProvider, extend, localize } from 'vee-validate';
import en from 'vee-validate/dist/locale/en.json';
import * as rules from 'vee-validate/dist/rules';


// install rules and localization
Object.keys(rules).forEach(rule => {
  extend(rule, rules[rule]);
});

localize('en', en);

Vue.config.productionTip = false


library.add(faUser, faFacebook,faGoogle,faLock,faTwitter,faEnvelope)
Vue.component('font-awesome-icons', FontAwesomeIcon)
// Install components globally
Vue.component('ValidationObserver', ValidationObserver);
Vue.component('ValidationProvider', ValidationProvider);
new Vue({
  vuetify,
  router,
  render: h => h(App)
})
.$mount('#app')
