from flask import jsonify, request, Blueprint
from .articulos_controller import ArticulosController

articulo_bp=Blueprint("articulo", __name__)

@articulo_bp.route("/articulos/", methods=['GET', 'OPTIONS'])
def get_all():
    try:
        articulos = ArticulosController.get_all()
        if articulos:
            return jsonify(articulos), 200
        else:
            return jsonify({'mensaje': 'no se encontraron articulos'}),404
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500
     
@articulo_bp.route("/articulos/<int:id>")
def get_one(id):
    try:
        articulo = ArticulosController.get_one(id)
        if articulo:
            return jsonify(articulo), 200
        else:
            return jsonify({'mensaje': 'no se encontro el articulo'}),404
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500  
@articulo_bp.route("/articulos/", methods=['POST', 'OPTIONS'])
def crear():
    try:
        data = request.get_json()
        if data is None:
            return  jsonify({'mensaje': "no se recibieron dato"})
        result = ArticulosController.crear(data)
        if result:
            return jsonify({'mensaje':'articulo creado correctamente'}), 201
        else:
            return jsonify({'mensaje': 'error al crear el articulo'}),500
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500
@articulo_bp.route("/articulos/<int:id>", methods=["PUT", "OPTIONS"])
def modificar_articulo(id):
    if request.method == "OPTIONS":
        return jsonify({'mensaje': 'ok'}), 200
    data = request.get_json()
    result = ArticulosController.update(id, data)
    if result:
        return {"mensaje": "Artículo actualizado correctamente"}, 200
    else:
        return {"mensaje": "Error al actualizar el artículo"}, 500     
@articulo_bp.route("/articulos/<int:id>", methods=["DELETE"])
def eliminar_articulo(id):
    result = ArticulosController.eliminar(id)
    if result:
        return {"mensaje": "Artículo eliminado correctamente"}, 200
    else:
        return {"mensaje": "Error al eliminar el artículo"}, 500
         