<template>
  <h1 class="titulo">Lista de Categorias</h1>
  <div class="crear-container">
  <router-link :to="{name:'categorias_create'}">CREAR</router-link>
</div>
  <table>
    <thead>
      <tr>
        <th>id</th>
        <th>nombre</th>
        <th>acciones</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="categoria in categorias" :key="categoria.id">
        <td>{{ categoria.id }}</td>
        <td>{{ categoria.nombre }}</td>
        <td>
          <router-link :to="{name:'categorias_update',params:{id:categoria.id}}">editar</router-link>
          <router-link :to="{name:'categorias_show',params:{id:categoria.id}}">mostrar</router-link>
          <button @click.prevent="eliminar(categoria.id as number)">Eliminar</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup lang="ts">
import { onMounted, toRefs } from 'vue'
import useCategoriasStore from '../../stores/categorias'
const { categorias } = toRefs(useCategoriasStore())
const { getAll, destroy } = useCategoriasStore()

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
