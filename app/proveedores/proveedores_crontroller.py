from .proveedores_model import ProveedoresModel
class ProveedoresController:
    @staticmethod
    def get_all():
        proveedores = ProveedoresModel.get_all()
        return proveedores

    @staticmethod    
    def get_one(id):
        proveedor = ProveedoresModel(id=id).get_by_id()
        return proveedor

    @staticmethod
    def crear(data: dict):
        print(data)
        proveedor = ProveedoresModel(nombre=data['nombre'],direccion=data['direccion'],telefono=data['telefono'],email=data['email'])
        result = proveedor.create()
        return result

    @staticmethod
    def modificar(data:dict):
        proveedor = ProveedoresModel.deserializar(data)
        result = proveedor.update()
        return result

    @staticmethod    
    def eliminar(id):
        result = ProveedoresModel.delete(id)
        return result