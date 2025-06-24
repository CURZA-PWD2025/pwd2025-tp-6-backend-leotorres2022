<template>
    <h1 class="titulo">Lista de Proveedores</h1>
  <div class="crear-container">

  <router-link :to="{name:'proveedores_create'}">CREAR</router-link>

</div>
  <table>
    <thead>
      <tr>
        <th>id</th>
        <th>nombre</th>
        <th>direccion</th>
        <th>telefono</th>
        <th>email</th>
        <th>acciones</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="proveedor in proveedores" :key="proveedor.id">
        <td>{{ proveedor.id }}</td>
        <td>{{ proveedor.nombre }}</td>
        <td>{{ proveedor.direccion }}</td>
        <td>{{ proveedor.telefono }}</td>
        <td>{{ proveedor.email }}</td>
        <td>
          <router-link :to="{name:'proveedores_update',params:{id:proveedor.id}}">editar</router-link>
          <router-link :to="{name:'proveedores_show',params:{id:proveedor.id}}">mostrar</router-link>
          <button @click.prevent="eliminar(proveedor.id as number)">Eliminar</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup lang="ts">
import { onMounted, toRefs } from 'vue'
import useProveedoresStore from '../../stores/proveedores'
const { proveedores } = toRefs(useProveedoresStore())
const { getAll, destroy } = useProveedoresStore()

onMounted(async () => {
  await getAll()
})
async function eliminar(id: number) {
  if (confirm('¿Estás seguro de eliminar esta categoria ' + id + '?')) {
    await destroy(id)
    await getAll()
  }
}
</script>

<style scoped>
.titulo {
  text-align: center;
  margin-top: 1rem;
}
.crear-container {
  display: flex;
  justify-content: center;
  margin-bottom: 1rem;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}
th, td {

  padding: 0.5rem;
  text-align: left;
  vertical-align: middle;
}
th {
  background: #f5f5f5;
}
/* Aplica flex solo a la celda de acciones */
td:last-child {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}
</style>
