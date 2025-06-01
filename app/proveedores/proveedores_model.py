from ..database.conect_db import ConectDB
import pymysql

class ProveedoresModel():

    def __init__(self, id:int=0, nombre:str="",telefono:str="",
                 direccion:str="", email:str=""):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

    def serializar(self) -> dict:
        return {
            'id': self.id,
            'nombre': self.nombre ,
            'telefono': self.telefono,
            'direccion': self.direccion,
            'email': self.email             
        }
    
    @staticmethod
    def deserializar(data:dict):
        return ProveedoresModel(
            id=data['id'], 
            nombre=data['nombre'],
            telefono=data['telefono'],
            direccion=data['direccion'],
            email=data['email']
        )
        
    @staticmethod
    def get_all():
        cnx = ConectDB.connect()
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
            try:
                cursor.execute("SELECT * FROM proveedores")
                rows = cursor.fetchall()
                proveedores = []
                for row in rows:
                    proveedores.append(row)
                return proveedores
            except Exception as exc:
                return {'mensaje': f" error al listar proveedores {exc}"}
    
    def get_by_id(self):
        cnx = ConectDB.connect()
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
            try:
                cursor.execute("SELECT * FROM proveedores WHERE id = %s", (self.id,))
                row = cursor.fetchone()
                if row:
                    return row
                return False
            except Exception as exc:
                print(f"Error al obtener proveedor por id {self.id}: {exc}")
              
    def create(self):
        cnx = ConectDB.connect()
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
            try:
                cursor.execute("INSERT INTO proveedores (nombre,telefono,direccion,email)  VALUES (%s, %s, %s, %s)", 
                               (self.nombre,self.telefono,
                                self.direccion,self.email))
                result = cursor.rowcount
                print("RESULTADO DE LA INSERCION:", result)
                cnx.commit()
                if result > 0:
                    return True
                return False
                
            except Exception as exc:
                cnx.rollback()
                print(f" error crear el proveedor {exc}")
            finally:
                cnx.close()
    def update(self):
        cnx = ConectDB.connect()
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
            try:
                cursor.execute("UPDATE proveedores SET nombre = %s ,telefono = %s, direccion = %s ,email = %s where id=%s ", 
                               (self.nombre,self.telefono,self.direccion,self.email, self.id))
                result = cursor.rowcount
                cnx.commit()
                
                if result > 0:
                    return True
                return False
                
            except Exception as exc:
                cnx.rollback()
                return {'mensaje':f" error actualizar un proveedor {exc}"}
            finally:
                cnx.close()                
    @staticmethod
    def delete(id:int):
        cnx = ConectDB.connect()
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
            try:
                cursor.execute("DELETE FROM proveedores where id = %s ", 
                               (id,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {'mensaje':f" error eliminar un proveedor {exc}"}
            finally:
                cnx.close()