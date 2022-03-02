/* import { processExpression } from '@vue/compiler-core' */
import { createRouter,createWebHistory  } from 'vue-router'
import Test1 from './components/test1.vue'
import Test2 from './components/test2.vue'
import HelloWorld from './components/HelloWorld.vue'

const routes = [
    { path: "/", component: Test1 },
    { path: "/test2", component: Test2 },
    { path: "/hello", component: HelloWorld },
  ];

const history = createWebHistory();

const router = createRouter({
    history,
    routes,
  });

export default router;