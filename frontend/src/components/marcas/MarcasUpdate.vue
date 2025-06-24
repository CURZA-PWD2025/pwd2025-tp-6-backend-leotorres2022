<template>
  <div>
<h2>Modificar la Marca</h2>
    <form @submit.prevent="editar">
      <div >
        <label for="" >Nombre de la Marca</label>
        <input type="text" name="" v-model="marca.nombre">
      </div>
      <button type="submit">Modificar</button>
    </form>
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

const editar = async () => {
  if (!marca.value.nombre) {
    alert('El nombre de la marca es obligatorio');
  } else {
    const response = await update(marca.value);
    alert('Marca actualizada correctamente');
    marca.value.nombre= ''
    console.log(response);
  }
};

</script>

<style scoped>

</style>
