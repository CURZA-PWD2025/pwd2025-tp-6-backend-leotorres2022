<template>
  <div>
<h2>Modificar el Articulo</h2>
    <form @submit.prevent="editar">
      <div >
        <label for="" >Descripcion del Articulo</label>
        <input type="text" name="" v-model="articulo.descripcion">
        <label for="" >Precio</label>
        <input type="text" name="" v-model="articulo.precio">
        <label for="" >Stock</label>
        <input type="text" name="" v-model="articulo.stock">
          <label>Marca:
      <select v-model="articulo.marca" required>
        <option v-for="marca in marcas" :key="marca.id" :value="marca">
          {{ marca.nombre }}
        </option>
      </select>
    </label>
     <div style="margin-top: 25px;">
    <label>Proveedor:
      <select v-model="articulo.proveedor" required>
        <option v-for="proveedor in proveedores" :key="proveedor.id" :value="proveedor">
          {{ proveedor.nombre }}
        </option>
      </select>
    </label>
    </div>
  <div style="margin-top: 25px;">
  <label>Categorías:
    <select v-model="articulo.categorias" multiple required>
      <option v-for="categoria in categorias" :key="categoria.id" :value="categoria">
        {{ categoria.nombre }}
      </option>
    </select>
  </label>
</div>
       </div>
      <button type="submit">Modificar</button>
    </form>
    <router-link :to="{name:'articulos_list'}">volver</router-link>
  </div>
</template>
<script setup lang="ts">
import { toRefs } from 'vue';
import  UseArticulosStore from '../../stores/articulos'
import  UseMarcasStore from '../../stores/marcas'
import  UseProveedoresStore from '../../stores/proveedores'
import  UseCategoriasStore from '../../stores/categorias'
import { useRoute} from 'vue-router';
import { onMounted } from 'vue';
const route = useRoute()
const { articulo,articulos} = toRefs(UseArticulosStore())
const { marcas, getAll: getAllMarcas } = UseMarcasStore()
const { proveedores, getAll: getAllProveedores } = UseProveedoresStore()
const { categorias, getAll: getAllCategorias } = UseCategoriasStore()
const { update } = UseArticulosStore()
onMounted(async () => {
 await getAllMarcas()
  await getAllProveedores()
  await getAllCategorias()
  const id = route.params.id
  console.log('ID de articulo a editar:', id)
const encontrada= articulos.value.find(articulo => articulo.id == parseInt(id as string))
articulo.value =  encontrada ?? { descripcion: '', precio: 0, stock: 0,marca:undefined,proveedor:undefined,categorias: [] };
})
const editar = async () => {
  if (!articulo.value.descripcion) {
    alert('la descripcion del articulo es obligatoria');
  } else {
    const articulo_json= {
      id: articulo.value.id,
      descripcion: articulo.value.descripcion,
      precio: Number(articulo.value.precio),
      stock: Number(articulo.value.stock),
      marca_id: articulo.value.marca?.id,
      proveedor_id: articulo.value.proveedor?.id,
      categorias: articulo.value.categorias?.map(cat => cat.id)
    }
    const response = await update(articulo_json)
    alert('Articulo actualizado correctamente')
    console.log(response)
  }
};
</script>

<style scoped>

</style>
