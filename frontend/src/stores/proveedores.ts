
import { defineStore } from "pinia"
import { ref } from "vue"
import ApiService from "@/services/ApiService"
import type  {Proveedores}   from '@/intefaces/Proveedores'

const useProveedoresStore = defineStore('proveedores', () => {
  const proveedores = ref<Array<Proveedores>>([])
  const proveedor= ref<Proveedores>({
    id: 0,
    nombre: '',
    direccion: '',
    email: '',
    telefono: ''
  })
const url = 'proveedores'
  async function getAll()
  {
    const data = await ApiService.getAll(url)
    if (data) {
      proveedores.value = data
              }
  }
  async function create(proveedor: Proveedores) {
    const response = await ApiService.create(url, proveedor)
    if (response) {
           return response
    }

  }

 async function update(proveedor: Proveedores) {
    if (proveedor.id) {
    const data = await ApiService.update(url +'/',proveedor.id, proveedor)
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
return { proveedores,proveedor , getAll, destroy, create, update }

})

export default useProveedoresStore
