
import { defineStore } from "pinia"
import { ref } from "vue"
import ApiService from "@/services/ApiService"
import type  {Articulos}   from '@/intefaces/Articulos'
import type {Marca} from '@/intefaces/Marca'
import type {Proveedores} from '@/intefaces/Proveedores'

const useArticulosStore = defineStore('articulos', () => {
  const articulos = ref<Array<Articulos>>([])
  const articulo = ref<Articulos>({
    id: 0,
    descripcion: '',
    precio: 0,
    stock: 0,
    marca: {} as Marca,
    proveedor: {} as Proveedores,
    categorias: []
  })
const url = 'articulos'
  async function getAll()
  {
    const data = await ApiService.getAll(url)
    if (data) {
      articulos.value = data
              }
  }
  async function create(articulo:Articulos) {
    const data = await ApiService.create(url+'/', articulo)
    if (data) {
           return data
    }

  }

 async function update(articulo: Articulos) {
    if (articulo.id) {
    const data = await ApiService.update(url+'/',articulo.id, articulo)
    if (data) {
      return data
    }
  }
  }

  async function destroy(id: number) {
    const data = await ApiService.destroy(url + '/', id)
    if (data) {
      return data
          }
  }
return { articulos, articulo, getAll, destroy, create, update }

})

export default useArticulosStore
