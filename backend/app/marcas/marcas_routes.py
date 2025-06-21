from .marcas_controller import MarcasController
from flask import Blueprint, jsonify, request

marca_bp = Blueprint('marca_bp', __name__)

@marca_bp.route("/marcas", methods=['GET'])

def get_all():
    try:
        marcas = MarcasController.get_all()
        if marcas:
            return jsonify(marcas), 200
        else:
            return jsonify({'mensaje': 'No hay marcas disponibles'}), 404
    except Exception as exc:
        return jsonify({'mensaje': f"Error al obtener marcas: {exc}"}), 500

@marca_bp.route("/marcas/<int:id>")
def get_one(id):
    try:
        categoria = MarcasController.get_one(id)
        if categoria:
            return jsonify(categoria), 200
        else:
            return jsonify({'mensaje': 'No se encontró la categoría'}), 404
    except Exception as exc:
        return jsonify({'mensaje': f"Error al obtener categoría: {exc}"}), 500

@marca_bp.route("/marcas/", methods=['POST'])
def crear():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'mensaje': "No se recibieron datos"})
        result = MarcasController.crear(data)
        if result:
            return jsonify({'mensaje':'Marca creada correctamente'}), 201
        else:
            return jsonify({'mensaje': 'Error al crear la marca'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500

@marca_bp.route("/marcas/<int:id>", methods=["PUT"])
def modificar(id):
    try:
        data = request.get_json()
        data['id'] = id
        result = MarcasController.modificar(data)
        if result:
            return jsonify({'mensaje':'Marca modificada correctamente'}), 200
        else:
            return jsonify({'mensaje': 'Error al modificar la marcas'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500    

@marca_bp.route("/marcas/<int:id>", methods=["DELETE"])
def eliminar(id):
    try:
        result = MarcasController.eliminar(id)
        if result:
            return jsonify({'mensaje':"marca eliminada con éxito"})
        else:
            return jsonify({'mensaje':"Error al eliminar la marca"})
    except Exception as exc:
        return jsonify({'mensaje':f"Error: {exc}"})