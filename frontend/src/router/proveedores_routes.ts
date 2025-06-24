const proveedores_routes = [
  {
    path: '/proveedores',
    name: 'proveedores',
    component: () => import('../views/ProveedoresView.vue'),
    children: [
      {
        path: '',
        name: 'proveedores_list',
        component: () => import('../components/proveedores/ProveedoresList.vue'),
      },
      {
        path: ':id/update',
        name: 'proveedores_update',
        component: () => import('../components/proveedores/ProveedoresUpdate.vue'),
      },
      {
        path: '',
        name: 'proveedores_create',
        component: () => import('../components/proveedores/ProveedoresCreate.vue'),
      },
      {
        path: ':id/show',
        name: 'proveedores_show',
        component: () => import('../components/proveedores/ProveedoresShow.vue'),
      },

    ]
  }
]
export default proveedores_routes
