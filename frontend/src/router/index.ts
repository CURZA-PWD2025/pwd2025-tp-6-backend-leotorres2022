import { createRouter, createWebHistory } from 'vue-router'
import marcas_routes from './marcas_routes'
import HomeView from '../views/HomeView.vue'
import categorias_routes from './categorias_routes'

const routes= [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
...marcas_routes,
...categorias_routes,
  ]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
routes ,
})

export default router
