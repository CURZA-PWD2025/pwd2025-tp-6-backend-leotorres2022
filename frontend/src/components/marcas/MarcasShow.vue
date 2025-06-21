<template>
  <div>
<h2>Detalle de laMarca</h2>
<h2>Nombre:{{ marca.nombre }}</h2>
<h4>Id:{{ marca.id }}</h4>
    <router-link :to="{name:'marcas_list'}">volver</router-link>
  </div>
</template>
<script setup lang="ts">
import { toRefs } from 'vue';
import  UseMarcasStore from '../../stores/marcas'
import { useRoute} from 'vue-router';
import { onMounted } from 'vue';
const route = useRoute()
const { marca,marcas} = toRefs(UseMarcasStore())
const {update} = UseMarcasStore()
onMounted(async () => {
  const id = route.params.id
  console.log('ID de la marca a editar:', id)
const encontrada= marcas.value.find(marca => marca.id == parseInt(id))
marca.value =  encontrada ?? { nombre: '' }
})

</script>

<style scoped>

</style>
