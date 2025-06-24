
import { defineStore } from "pinia"
import { ref } from "vue"
import ApiService from "@/services/ApiService"
import type  {Marca}   from '@/intefaces/Marca'

const useMarcasStore = defineStore('marcas', () => {
  const marcas = ref<Array<Marca>>([])
  const marca = ref<Marca>({
    id: 0,
    nombre: '',
  })
const url = 'marcas'
  async function getAll()
  {
    const data = await ApiService.getAll(url)
    if (data) {
      marcas.value = data
              }
  }
  async function create(marca:Marca) {
    const response = await ApiService.create(url, marca)
    if (response) {
           return response
    }

  }

 async function update(marca: Marca) {
    if (marca.id) {
    const data = await ApiService.update(url +'/',marca.id, marca)
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
return { marcas, marca, getAll, destroy, create, update }

})

export default useMarcasStore
