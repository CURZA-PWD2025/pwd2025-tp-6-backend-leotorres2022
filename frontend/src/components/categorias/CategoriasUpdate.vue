<template>
  <div>
<h2>Modificar la Categoria</h2>
    <form @submit.prevent="editar">
      <div >
        <label for="" >Nombre de la Categoria</label>
        <input type="text" name="" v-model="categoria.nombre">
      </div>
      <button type="submit">Modificar</button>
    </form>
    <router-link :to="{name:'categorias_list'}">volver</router-link>
  </div>
</template>
<script setup lang="ts">
import { toRefs } from 'vue';
import  UseCategoriasStore from '../../stores/categorias'
import { useRoute} from 'vue-router';
import { onMounted } from 'vue';
const route = useRoute()
const { categoria,categorias} = toRefs(UseCategoriasStore())
const {update} = UseCategoriasStore()
onMounted(async () => {
  const id = route.params.id
  console.log('ID de la marca a editar:', id)
const encontrada= categorias.value.find(categoria => categoria.id == parseInt(id as string));
categoria.value =  encontrada ?? { nombre: '' }
})

const editar = async () => {
  if (!categoria.value.nombre) {
    alert('El nombre de la categoria es obligatorio');
  } else {
    const response = await update(categoria.value);
    alert('Categoria actualizada correctamente');
    categoria.value.nombre= ''
    console.log(response);
  }
};

</script>

<style scoped>

</style>
