from .marcas_model import MarcasModel
class MarcasController:
    @staticmethod
    def get_all():
        marcas = MarcasModel.get_all()
        return marcas

    @staticmethod    
    def get_one(id):
        marca = MarcasModel(id=id).get_by_id()
        return marca

    @staticmethod
    def crear(data: dict):
        print(data)
        marca = MarcasModel(nombre=data['nombre'])
        result = marca.create()
        return result

    @staticmethod
    def modificar(data:dict):
        marca = MarcasModel.deserializar(data)
        result = marca.update()
        return result

    @staticmethod    
    def eliminar(id):
        result = MarcasModel.delete(id)
        return result