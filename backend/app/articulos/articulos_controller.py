
from .articulos_model import ArticulosModel
from ..marcas.marcas_model import MarcasModel as Marca
from ..proveedores.proveedores_model import ProveedoresModel as Proveedor
from ..categorias.categorias_model import CategoriasModel as Categorias


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
    def crear(data: dict):
        marca_data = Marca(id=data['marca_id']).get_by_id()
        proveedor_data = Proveedor(id=data['proveedor_id']).get_by_id()
        marca = Marca.deserializar(marca_data) if marca_data else None
        proveedor = Proveedor.deserializar(proveedor_data) if proveedor_data else None
        categorias = []
        if 'categorias' in data and isinstance(data['categorias'], list):
          for cat_id in data['categorias']:
           categorias.append(Categorias(id=cat_id))

        articulo = ArticulosModel(
            descripcion=data['descripcion'],
            precio=data['precio'],
            stock=data['stock'],
            marca=marca,
            proveedor=proveedor,
            categorias=categorias
                               )
        result = articulo.create()
        return result
    @staticmethod
    def update(id, data: dict):
     marca_data = Marca(id=data['marca_id']).get_by_id()
     proveedor_data = Proveedor(id=data['proveedor_id']).get_by_id()
     marca = Marca.deserializar(marca_data) if marca_data else None
     proveedor = Proveedor.deserializar(proveedor_data) if proveedor_data else None
     categorias = []
     if 'categorias' in data and isinstance(data['categorias'], list):
        for cat_id in data['categorias']:
            categorias.append(Categorias(id=cat_id))
        articulo = ArticulosModel(
        id=id,
        descripcion=data['descripcion'],
        precio=data['precio'],
        stock=data['stock'],
        marca=marca,
        proveedor=proveedor,
        categorias=categorias
     )
     result = articulo.update()
     return result
    @staticmethod
    def eliminar(id):
     articulo = ArticulosModel(id=id)
     return articulo.delete()
    
    