<template>
<div class="crear-container">
    <router-link :to="{name:'marcas_create'}">CREAR</router-link>
  </div>
<tbody>
   <tr>
  <th>id</th>
  <th>nombre</th>
  <th>acciones</th>
 </tr>
  <tr v-for="marca in marcas"  :key="marca.id">
    <td>{{ marca.id}}</td>
    <td>{{ marca.nombre }}</td>

    <td>
       <router-link :to="{name:'marcas_update',params:{id:marca.id}}">editar</router-link>
       <router-link :to="{name:'marcas_show',params:{id:marca.id}}">mostrar</router-link>
      <button @click.prevent="eliminar(marca.id as number)">Eliminar</button>

    </td>
  </tr>

</tbody>
</template>

<script setup lang="ts">
import { onMounted,toRefs } from 'vue'
import  useMarcasStore from '../../stores/marcas'
const {marcas}= toRefs(useMarcasStore())
const {getAll,destroy} = useMarcasStore()

onMounted(async () => {
  await getAll()
})
async function eliminar(id:number) {
  if (confirm('¿Estás seguro de eliminar esta marca'+id+'?'))
   {
    await destroy(id);
    await getAll();
  }

}
</script>

<style scoped>
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
