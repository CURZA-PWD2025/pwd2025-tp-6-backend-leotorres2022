from flask import Flask
from flask_cors import CORS
from .categorias.categorias_routes import categoria_bp
from .marcas.marcas_routes import marca_bp
from .proveedores.proveedores_routes import proveedor_bp
from .articulos.articulos_routes import articulo_bp


def create_app():
    app= Flask(__name__)
    CORS(app)  
    app.register_blueprint(categoria_bp)
    app.register_blueprint(marca_bp)
    app.register_blueprint(proveedor_bp)
    app.register_blueprint(articulo_bp)
    @app.route("/")
    def home():
        return    "<h1>Hola bienvenidos a la pagina</h1>"
    return app
      