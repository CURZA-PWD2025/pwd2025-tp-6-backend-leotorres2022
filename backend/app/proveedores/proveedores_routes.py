from .proveedores_crontroller import ProveedoresController
from flask import Blueprint, jsonify, request

proveedor_bp = Blueprint('proveedor_bp', __name__)

@proveedor_bp.route("/proveedores")
def get_all():
    try:
        proveedores = ProveedoresController.get_all()
        if proveedores:
            return jsonify(proveedores), 200
        else:
            return jsonify({'mensaje': 'No hay proveedores disponibles'}), 404
    except Exception as exc:
        return jsonify({'mensaje': f"Error al obtener proveedores: {exc}"}), 500

@proveedor_bp.route("/proveedores/<int:id>")
def get_one(id):
    try:
        proveedor = ProveedoresController.get_one(id)
        if proveedor:
            return jsonify(proveedor), 200
        else:
            return jsonify({'mensaje': 'No se encontró el proveedor'}), 404
    except Exception as exc:
        return jsonify({'mensaje': f"Error al obtener proveedor: {exc}"}), 500

@proveedor_bp.route("/proveedores/", methods=['POST'])
def crear():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'mensaje': "No se recibieron datos"})
        result = ProveedoresController.crear(data)
        if result:
            return jsonify({'mensaje':'proveedor creada correctamente'}), 201
        else:
            return jsonify({'mensaje': 'Error al crear la proveedor'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500

@proveedor_bp.route("/proveedores/<int:id>", methods=["PUT"])
def modificar(id):
    try:
        data = request.get_json()
        data['id'] = id
        result = ProveedoresController.modificar(data)
        if result:
            return jsonify({'mensaje':'proveedor modificado correctamente'}), 200
        else:
            return jsonify({'mensaje': 'Error al modificar  proveedor'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500    

@proveedor_bp.route("/proveedores/<int:id>", methods=["DELETE"])
def eliminar(id):
    try:
        result = ProveedoresController.eliminar(id)
        if result:
            return jsonify({'mensaje':"proveedor eliminado con éxito"})
        else:
            return jsonify({'mensaje':"Error al eliminar proveedor"})
    except Exception as exc:
        return jsonify({'mensaje':f"Error: {exc}"})