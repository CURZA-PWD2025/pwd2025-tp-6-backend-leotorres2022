<template>
  <div>
    <form @submit.prevent="crear">
      <div >
        <label for="" >Nombre del proveedor</label>
        <input type="text" name="create" v-model="proveedor.nombre">
        <label for="" >Telefono</label>
        <input type="text" name="create" v-model="proveedor.telefono">
        <label for="" >Direccion</label>
        <input type="text" name="create" v-model="proveedor.direccion">
        <label for="" >Email</label>
        <input type="email" name="create" v-model="proveedor.email">
      </div>
      <button type="submit">Crear Proveedor</button>
    </form>
    <router-link :to="{name:'proveedores_list'}">volver</router-link>
  </div>
</template>

<script setup lang="ts">
import { toRefs} from 'vue'
import  UseProveedoresStore from '../../stores/proveedores'
const {proveedor} = toRefs(UseProveedoresStore())
const {create} = UseProveedoresStore()
const crear = async ()=> {
  if (!proveedor.value.nombre)  {
    alert('El nombre del proveedor es obligatorio')
  }
  else if (!proveedor.value.telefono) {
    alert('El telefono del proveedor es obligatorio')
  }
  else if (!proveedor.value.direccion) {
    alert('La direccion del proveedor es obligatoria')
  }
  else if (!proveedor.value.email) {
    alert('El email del proveedor es obligatorio')
  }
else
  {
    const response = await create(proveedor.value)
    proveedor.value.nombre= ''
    proveedor.value.telefono= ''
    proveedor.value.direccion= ''
    proveedor.value.email= ''
    alert('Proveedor creado correctamente')
    console.log(response)
  }
}

</script>

<style scoped>

</style>
