<template>
  <div>
<h2>Detalle del Proveedor</h2>
<h3>Nombre: <span class="dato">{{ proveedor.nombre }}</span></h3>
<h3>Direccion: <span class="dato">{{ proveedor.direccion }}</span></h3>
<h3>Telefono: <span class="dato">{{ proveedor.telefono }}</span></h3>
<h3>Email:<span class="dato">{{ proveedor.email }}</span></h3>
<h4>Id: <span class="dato">{{ proveedor.id }}</span></h4>
    <router-link :to="{name:'proveedores_list'}">volver</router-link>
  </div>
</template>
<script setup lang="ts">
import { toRefs } from 'vue';
import  UseProveedoresStore from '../../stores/proveedores'
import { useRoute} from 'vue-router';
import { onMounted } from 'vue';
const route = useRoute()
const { proveedor: proveedor,proveedores} = toRefs(UseProveedoresStore())
onMounted(async () => {
const id = route.params.id
const encontrada= proveedores.value.find(proveedor => proveedor.id == parseInt(id as string))
proveedor.value =  encontrada ?? { nombre: '' , direccion: '', telefono: '', email: '' }
if (!proveedor.value) {
    console.error('Proveedor no encontrado')
  }
})

</script>

<style scoped>
.dato {
  color: #1976d2;
  font-weight: bold;
  padding: 0.2em 0.5em;
  border-radius: 4px;
}

</style>
