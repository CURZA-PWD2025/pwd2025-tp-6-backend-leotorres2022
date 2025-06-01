from ..database.conect_db import ConectDB
from ..marcas.marcas_model import MarcasModel as Marca
from ..proveedores.proveedores_model import ProveedoresModel as Proveedor
import pymysql

class ArticulosModel():

    def __init__(self, id:int=0, descripcion:str="",marca:Marca = None ,
                 precio:float=0.0,proveedor:Proveedor=None ,stock:int=0 ):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca = marca
        self.proveedor = proveedor
        
    def serializar(self) -> dict:
        return {
               'id': self.id,
                'descripcion': self.descripcion,
                'precio': self.precio,
                'stock': self.stock,
                'marca': self.marca.serializar() if self.marca else None,
                'proveedor': self.proveedor.serializar() if self.proveedor else None           
        }
    
    @staticmethod
    def deserializar(data:dict):
        return ArticulosModel(
            id=data['id'], 
            descripcion=data['descripcion'],
            precio=data['precio'], 
            stock=data['stock'],
            marca=data['marca'],
            proveedor=data['proveedor'] 
        )
        
    @staticmethod
    def get_all():
     cnx = ConectDB.connect()
     with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
        try:
            cursor.execute("SELECT * FROM articulos")
            rows = cursor.fetchall()
            articulos = []
            for row in rows:
                marca = Marca(id=row['marca_id']).get_by_id()
                proveedor = Proveedor(id=row['proveedor_id']).get_by_id()
                articulo = ArticulosModel(
                    id=row['id'],
                    descripcion=row['descripcion'],
                    precio=row['precio'],
                    stock=row['stock'],
                    marca=Marca.deserializar(marca) if marca else None,
                    proveedor=Proveedor.deserializar(proveedor) if proveedor else None
                )
                articulos.append(articulo.serializar())
            return articulos
        except Exception as exc:
            return {'mensaje': f" error al listar articulos {exc}"}
        finally:
            cnx.close()
    @staticmethod       
    def get_by_id(self):
     cnx = ConectDB.connect()
     with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
        try:
            cursor.execute("SELECT * FROM articulos where id = %s", (self.id,))
            row = cursor.fetchone()
            print("Row encontrado:", row)
            if row:
                marca = Marca(id=row['marca_id']).get_by_id()
                proveedor = Proveedor(id=row['proveedor_id']).get_by_id()
                row['marca'] = Marca.deserializar(marca) if marca else None
                row['proveedor'] = Proveedor.deserializar(proveedor) if proveedor else None
                row = ArticulosModel.deserializar(row)
                return row.serializar()
            return False
        except Exception as exc:
            print("Error en get_by_id:", exc)
            return {'mensaje':f" error buscar un articulo {exc}"}
        finally:
            cnx.close() 
    def create(self):
        cnx = ConectDB.connect()
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
            try:
                cursor.execute("INSERT INTO articulos (descripcion,precio,stock,marca_id,proveedor_id)  VALUES (%s, %s, %s, %s, %s)", 
                              (self.descripcion, self.precio, self.stock, self.marca.id, self.proveedor.id))
                result = cursor.rowcount
                print("RESULTADO DE LA INSERCION:", result)
                cnx.commit()
                if result > 0:
                    return True
                return False
                
            except Exception as exc:
                cnx.rollback()
                print(f" error crear el articulo {exc}")
            finally:
                cnx.close()
