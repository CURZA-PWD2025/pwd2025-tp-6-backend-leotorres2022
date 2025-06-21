const marcas_routes = [
  {
    path: '/marcas',
    name: 'marcas',
    component: () => import('../views/MarcasView.vue'),
    children: [
      {
        path: '',
        name: 'marcas_list',
        component: () => import('../components/marcas/MarcasList.vue'),
      },
      {
        path: ':id/update',
        name: 'marcas_update',
        component: () => import('../components/marcas/MarcasUpdate.vue'),
      },
      {
        path: '',
        name: 'marcas_create',
        component: () => import('../components/marcas/MarcasCreate.vue'),
      },
      {
        path: ':id/show',
        name: 'marcas_show',
        component: () => import('../components/marcas/MarcasShow.vue'),
      },

    ]
  }
]

export default marcas_routes
