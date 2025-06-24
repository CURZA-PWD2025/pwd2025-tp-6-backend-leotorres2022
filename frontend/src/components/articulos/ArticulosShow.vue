<template>
  <div>
<h2>Detalle del Articulo</h2>
<h3>Descripcion: <span class="dato">{{ articulo.descripcion }}</span></h3>
<h3>Precio: <span class="dato">{{ articulo.precio }}</span></h3>
<h3>Stock: <span class="dato">{{ articulo.stock }}</span></h3>
<h3>Marca: <span class="dato">{{ articulo.marca?.nombre || 'Sin marca' }}</span></h3>
<h3>Proveedor: <span class="dato">{{ articulo.proveedor?.nombre || 'Sin proveedor' }}</span></h3>
<h3>Categorias:
  <span class="dato">
    {{ articulo.categorias && articulo.categorias.length
      ? articulo.categorias.map(c => c.nombre).join(', ')
      : 'Sin categorías' }}
  </span>
</h3>
<h4>Id: <span class="dato">{{ articulo.id }}</span></h4>
    <router-link :to="{name:'articulos_list'}">volver</router-link>
  </div>
</template>
<script setup lang="ts">
import { toRefs } from 'vue';
import useArticulosStore from '../../stores/articulos';
import { useRoute} from 'vue-router';
import { onMounted } from 'vue';

const route = useRoute()
const { articulo: articulo ,articulos} = toRefs(useArticulosStore())
const {update} = useArticulosStore()

onMounted(async () => {
const id = route.params.id
const encontrada= articulos.value.find(articulo => articulo.id == parseInt(id as string))
articulo.value =  encontrada ?? { descripcion: '' , precio: 0, stock: 0, marca:undefined , proveedor: undefined ,categorias:[]}
if (!articulo.value) {
    console.error('Articulo no encontrado')
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
