<template>
  <div>
<h2>Modificar Proveedor</h2>
    <form @submit.prevent="editar">
      <div >
        <label for="" >Nombre del proveedor</label>
        <input type="text" name="" v-model="proveedor.nombre">
         <label for="" >Telefono</label>
        <input type="text" name="" v-model="proveedor.telefono">
         <label for="" >Direccion</label>
        <input type="text" name="" v-model="proveedor.direccion">
          <label for="" >Email</label>
        <input type="email" name="" v-model="proveedor.email">

      </div>
      <button type="submit">Modificar</button>
    </form>
    <router-link :to="{name:'proveedores_list'}">volver</router-link>
  </div>
</template>
<script setup lang="ts">
import { toRefs } from 'vue';
import  UseProveedoresStore from '../../stores/proveedores'
import { useRoute} from 'vue-router';
import { onMounted } from 'vue';
const route = useRoute()
const { proveedor,proveedores} = toRefs(UseProveedoresStore())
const {update} = UseProveedoresStore()
onMounted(async () => {
  const id = route.params.id
  console.log('ID del proveedor a editar:', id)
const encontrada=proveedores.value.find(proveedor => proveedor.id == parseInt(id as string))
proveedor.value =  encontrada ?? { nombre: '' , direccion: '', telefono: '', email: '' }
})

const editar = async () => {
  if (!proveedor.value.nombre) {
    alert('El nombre del proveedor es obligatorio');
  } else {
    const response = await update(proveedor.value);
    proveedor.value.nombre= ''
    proveedor.value.telefono= ''
    proveedor.value.direccion= ''
    proveedor.value.email= ''
    alert('Proveedor actualizado correctamente');
    console.log(response);
  }
};

</script>

<style scoped>

</style>
