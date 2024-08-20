import { createApp } from 'vue'
import router from './router/router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import App from './App.vue'
import './style.css'

axios.defaults.baseURL = import.meta.env.VITE_BACKEND
axios.defaults.headers['Accept'] = "application/json";
axios.defaults.headers['Content-Type'] = "application/json; charset=UTF-8";
axios.defaults.timeout = 5000;

createApp(App)
    .use(router)
    .use(VueAxios, axios)
    .mount('#app')
