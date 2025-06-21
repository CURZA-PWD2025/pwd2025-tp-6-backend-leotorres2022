<template>
  <div>
<h2>Detalle de la Categoria</h2>
<h2>Nombre:{{ categoria.nombre }}</h2>
<h4>Id:{{ categoria.id }}</h4>
    <router-link :to="{name:'categorias_list'}">volver</router-link>
  </div>
</template>
<script setup lang="ts">
import { toRefs } from 'vue';
import  UseCategoriasStore from '../../stores/categorias'
import { useRoute} from 'vue-router';
import { onMounted } from 'vue';
const route = useRoute()
const { categoria: categoria,categorias} = toRefs(UseCategoriasStore())
const {update} = UseCategoriasStore()
onMounted(async () => {
  const id = route.params.id
  console.log('ID de la categoria a editar:', id)
const encontrada= categorias.value.find(categoria => categoria.id == parseInt(id))
categoria.value =  encontrada ?? { nombre: '' }
})

</script>

<style scoped>

</style>
