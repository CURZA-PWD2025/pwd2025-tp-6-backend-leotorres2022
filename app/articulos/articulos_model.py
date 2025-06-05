from ..database.conect_db import ConectDB
from ..marcas.marcas_model import MarcasModel as Marca
from ..proveedores.proveedores_model import ProveedoresModel as Proveedor
from   ..categorias.categorias_model import CategoriasModel as Categorias
import pymysql

class ArticulosModel():

    def __init__(self, id:int=0, descripcion:str="",marca:Marca = None ,
                 precio:float=0.0,proveedor:Proveedor=None ,stock:int=0,categorias:list[Categorias]=None):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca = marca
        self.proveedor = proveedor
        self.categorias = categorias
        
    def serializar(self) -> dict:
        return {
               'id': self.id,
                'descripcion': self.descripcion,
                'precio': self.precio,
                'stock': self.stock,
                'marca': self.marca.serializar() if self.marca else None,
                'proveedor': self.proveedor.serializar() if self.proveedor else None, 
                'categorias': [categoria.serializar() for categoria in self.categorias]
         
        }  
    
    @staticmethod
    def deserializar(data:dict):
        return ArticulosModel(
          **data  
        )
        
    @staticmethod
    def get_all() -> list[dict]:
     cnx = ConectDB.connect()
     try:
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM categorias")
            todas_categorias_rows = cursor.fetchall()
            todas_categorias = [Categorias.deserializar(cat) for cat in todas_categorias_rows]

           
            cursor.execute("SELECT * FROM articulos")
            rows = cursor.fetchall()
            articulos = []
            for row in rows:
              
                marca = Marca(id=row['marca_id']).get_by_id()
                proveedor = Proveedor(id=row['proveedor_id']).get_by_id()
                marca = Marca.deserializar(marca) if marca else None
                proveedor = Proveedor.deserializar(proveedor) if proveedor else None

                
                articulo = ArticulosModel(
                    id=row['id'],
                    descripcion=row['descripcion'],
                    precio=row['precio'],
                    stock=row['stock'],
                    marca=marca,
                    proveedor=proveedor,
                    categorias=todas_categorias
                )
                articulos.append(articulo.serializar())
            return articulos
     except Exception as exc:
        print(f"Error al listar articulos: {exc}")
        return {'mensaje': f" error al listar articulos {exc}"}
     finally:
        cnx.close()
        
    def get_by_id(self)->dict:
     cnx = ConectDB.connect()
     try:
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM articulos WHERE id = %s", (self.id,))
            row = cursor.fetchone()
            print("Row encontrado:", row)
            if not row:
                return False

            
            marca = Marca(id=row['marca_id']).get_by_id()
            proveedor = Proveedor(id=row['proveedor_id']).get_by_id()
            marca = Marca.deserializar(marca) if marca else None
            proveedor = Proveedor.deserializar(proveedor) if proveedor else None

            
            cursor.execute("SELECT categoria_id FROM articulos_categorias WHERE articulo_id = %s", (self.id,))
            categoria_ids = [cat['categoria_id'] for cat in cursor.fetchall()]
            categorias = []
            for cat_id in categoria_ids:
                cursor.execute("SELECT * FROM categorias WHERE id = %s", (cat_id,))
                cat_row = cursor.fetchone()
                if cat_row:
                    categorias.append(Categorias.deserializar(cat_row))

            articulo = ArticulosModel(
                id=row['id'],
                descripcion=row['descripcion'],
                precio=row['precio'],
                stock=row['stock'],
                marca=marca,
                proveedor=proveedor,
                categorias=categorias
            )
                       
            return articulo.serializar()
     except Exception as exc:
           print("Error en get_by_id:", exc)
           return {'mensaje': f" error buscar un articulo {exc}"}
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
