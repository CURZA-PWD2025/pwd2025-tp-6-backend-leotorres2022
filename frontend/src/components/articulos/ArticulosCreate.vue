<template>
  <div>
<h2>Crear articulo</h2>
    <form @submit.prevent="crear">
      <div >
        <label for="" >Descripcion del Articulo</label>
        <input type="text" name="create" v-model="articulo.descripcion">
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
    </label>
       </div>
      <button type="submit">Crear Articulo</button>
    </form>
    <router-link :to="{name:'articulos_list'}">volver</router-link>
  </div>
</template>

<script setup lang="ts">
import { toRefs} from 'vue'
import  UseArticulosStore from '../../stores/articulos'
import  UseMarcasStore from '../../stores/marcas'
import  UseProveedoresStore from '../../stores/proveedores'
import  UseCategoriasStore from '../../stores/categorias'
const { marcas, getAll: getAllMarcas } = UseMarcasStore()
const { proveedores, getAll: getAllProveedores } = UseProveedoresStore()
const { categorias, getAll: getAllCategorias } = UseCategoriasStore()
const {articulo} = toRefs(UseArticulosStore())
const {create} = UseArticulosStore()
import { onMounted } from 'vue'
onMounted(async () => {
await getAllMarcas()
await getAllProveedores()
await getAllCategorias()

  articulo.value = { descripcion: '', precio: 0, stock: 0, marca: undefined, proveedor: undefined , categorias: [] }
})

const crear = async ()=> {
  if (!articulo.value.descripcion) {
    alert('La descripcion del articulo es obligatoria')
    }
  else if (articulo.value.precio <= 0) {
    alert('El precio debe ser mayor a 0')
  }
  else if (articulo.value.stock < 0) {
    alert('El stock no puede ser negativo')
  }
  else if (!articulo.value.marca) {
    alert('Debe seleccionar una marca')
  }
  else if (!articulo.value.proveedor) {
    alert('Debe seleccionar un proveedor')
  }
 else if (!Array.isArray(articulo.value.categorias) || articulo.value.categorias.length === 0) {
  alert('Debe seleccionar al menos una categoría')
}
else {
    const articulo_json = {
      descripcion: articulo.value.descripcion,
      precio: Number(articulo.value.precio),
      stock: Number(articulo.value.stock),
      marca_id: articulo.value.marca?.id,
      proveedor_id: articulo.value.proveedor?.id,
      categorias: articulo.value.categorias?.map(cat => cat.id)
    }
    console.log('Articulo a crear:', articulo_json)
    try {
      await create(articulo_json)
      console.log('Articulo creado correctamente:', articulo_json)
      alert('Articulo creado correctamente')
      // Resetear los campos del formulario
      articulo.value.descripcion= ''
      articulo.value.precio= 0
      articulo.value.stock= 0
      articulo.value.marca= undefined
      articulo.value.proveedor= undefined
      articulo.value.categorias= []
    } catch (error) {
      console.error('Error al crear el artículo:', error)
      alert('Error al crear el artículo. Revisa la consola para más detalles.')
    }
  }
}

</script>

<style scoped>

</style>
