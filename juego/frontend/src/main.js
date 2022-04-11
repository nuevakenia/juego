import { createApp, VueElement } from 'vue'
import App from './App.vue'
import Test1 from './components/Test1.vue'
import router from './routes.js'


import 'bootstrap/dist/css/bootstrap.min.css'

createApp(Test1)
  .use(router)
  .mount("#app");