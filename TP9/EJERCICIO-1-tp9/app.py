from flask import Flask
from rutas.libros import libros_bp

app = Flask(__name__)

# Registrar blueprint
app.register_blueprint(libros_bp)

if __name__ == '__main__':
    app.run(debug=True)
