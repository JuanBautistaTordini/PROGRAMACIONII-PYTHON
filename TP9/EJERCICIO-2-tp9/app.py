# app.py

from flask import Flask

from rutas.routesSocio import socios_bp

app = Flask(__name__)

# Registrar el blueprint
app.register_blueprint(socios_bp)

if __name__ == '__main__':
    app.run(debug=True)
    