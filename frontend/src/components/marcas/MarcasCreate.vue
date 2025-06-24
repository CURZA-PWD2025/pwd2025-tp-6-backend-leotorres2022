<template>
  <div>
<h2>Componente para crear la Marca</h2>
    <form @submit.prevent="crear">
      <div >
        <label for="" >Nombre de la Marca</label>
        <input type="text" name="create" v-model="marca.nombre">
      </div>
      <button type="submit">Crear Marca</button>
    </form>
    <router-link :to="{name:'marcas_list'}">volver</router-link>
  </div>
</template>

<script setup lang="ts">
import { toRefs} from 'vue'
import  UseMarcasStore from '../../stores/marcas'
const {marca} = toRefs(UseMarcasStore())
const {create} = UseMarcasStore()
const crear = async ()=> {
  if (!marca.value.nombre) {
    alert('El nombre de la marca es obligatorio')
  }
else
  {
    const response = await create(marca.value)
    marca.value.nombre= ''
    alert('Marca creada correctamente')
    console.log(response)
  }
}

</script>

<style scoped>

</style>
