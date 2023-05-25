// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import ElCard from 'element-ui/packages/card';
import ElRow from 'element-ui/packages/row';
import ElCol from 'element-ui/packages/col';
import ElContainer from 'element-ui/packages/container'
import ElAside from 'element-ui/packages/aside'
import ElHeader from 'element-ui/packages/header'
import ElMain from 'element-ui/packages/main'
import 'element-ui/lib/theme-chalk/index.css'
import './global.css'

Vue.config.productionTip = false
Vue.use(ElCard)
Vue.use(ElRow)
Vue.use(ElCol)
Vue.use(ElContainer)
Vue.use(ElAside)
Vue.use(ElHeader)
Vue.use(ElMain)
Vue.use(axios)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
