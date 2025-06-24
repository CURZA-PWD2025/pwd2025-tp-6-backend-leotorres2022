const articulos_routes = [
  {
    path: '/articulos',
    name: 'articulos',
    component: () => import('../views/ArticulosView.vue'),
    children: [
      {
        path: '',
        name: 'articulos_list',
        component: () => import('../components/articulos/ArticulosList.vue'),
      },
      {
        path: ':id/update',
        name: 'articulos_update',
        component: () => import('../components/articulos/ArticulosUpdate.vue'),
      },
      {
        path: '',
        name: 'articulos_create',
        component: () => import('../components/articulos/ArticulosCreate.vue'),
      },
      {
        path: ':id/show',
        name: 'articulos_show',
        component: () => import('../components/articulos/ArticulosShow.vue'),
      },

    ]
  }
]
export default articulos_routes
