
from .articulos_model import ArticulosModel
from ..marcas.marcas_model import MarcasModel as Marca
from ..proveedores.proveedores_model import ProveedoresModel as Proveedor


class ArticulosController:
    
    @staticmethod
    def get_all():
        articulos = ArticulosModel.get_all()
        return articulos
    @staticmethod
    def get_one(id):
        articulo = ArticulosModel(id=id).get_by_id()
        return articulo
    
    @staticmethod
    @staticmethod
    def crear(data:dict):
       marca_data = Marca(id=data['marca_id']).get_by_id()
       proveedor_data = Proveedor(id=data['proveedor_id']).get_by_id()
       marca = Marca.deserializar(marca_data) if marca_data else None
       proveedor = Proveedor.deserializar(proveedor_data) if proveedor_data else None
       articulo = ArticulosModel( descripcion=data['descripcion'], precio=data['precio'], stock=data['stock'], marca=marca,proveedor=proveedor)
       result= articulo.create()
       return result