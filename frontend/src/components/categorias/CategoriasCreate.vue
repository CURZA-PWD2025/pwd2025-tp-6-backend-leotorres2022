<template>
  <div>
<h2>Componente para crear la Categoria</h2>
    <form @submit.prevent="crear">
      <div >
        <label for="" >Nombre de la Categoria</label>
        <input type="text" name="create" v-model="categoria.nombre">
      </div>
      <button type="submit">Crear Categoria</button>
    </form>
    <router-link :to="{name:'categorias_list'}">volver</router-link>
  </div>
</template>

<script setup lang="ts">
import { toRefs} from 'vue'
import  UseCategoriasStore from '../../stores/categorias'
const {categoria} = toRefs(UseCategoriasStore())
const {create} = UseCategoriasStore()
const crear = async ()=> {
  if (!categoria.value.nombre) {
    alert('El nombre de la marca es obligatorio')
  }
else
  {
    const response = await create(categoria.value)
    categoria.value.nombre= ''
    alert('Categoria creada correctamente')
    console.log(response)
  }
}

</script>

<style scoped>

</style>
