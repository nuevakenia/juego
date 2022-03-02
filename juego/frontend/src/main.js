import { createApp, VueElement } from 'vue'
import App from './App.vue'
import router from './routes.js'
import 'bootstrap/dist/css/bootstrap.min.css'

createApp(App)
  .use(router)
  .mount("#app");