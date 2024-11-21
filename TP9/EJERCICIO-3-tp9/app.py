from flask import Flask
from rutas.routesSocio import socios_bp
from rutas.routesPrestamo import prestamos_bp

#Crear la aplicación
app = Flask(__name__)

#Registrar los blueprints
app.register_blueprint(socios_bp)
app.register_blueprint(prestamos_bp)

if __name__ == '__main__':
    app.run(debug=True)
