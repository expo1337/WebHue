import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store.js'

import 'bootstrap/dist/css/bootstrap.css'
//import '@/theme/custom.scss'
import bootstrap from 'bootstrap/dist/js/bootstrap.js'
//import bootstrap from 'bootstrap'
import VueApexCharts from "vue3-apexcharts";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";

import {library} from "@fortawesome/fontawesome-svg-core";
import { faBluetooth } from '@fortawesome/free-brands-svg-icons'


import {faAngleDoubleLeft, faHouse, faPlus, faServer, faCircleInfo, faRightFromBracket} from "@fortawesome/free-solid-svg-icons";
library.add(faAngleDoubleLeft, faHouse, faPlus, faServer, faCircleInfo, faRightFromBracket,faBluetooth)

const app = createApp(App).use(store).use(bootstrap).use(router).use(VueApexCharts).component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
app.config.globalProperties.$bootstrap = bootstrap