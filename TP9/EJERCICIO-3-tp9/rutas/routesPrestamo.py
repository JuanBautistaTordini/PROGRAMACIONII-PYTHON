# a)Consultar todos los préstamos (GET)
# b)Buscar préstamo por socio DNI y libro ISBN (GET)
# c)Agregar un nuevo préstamo (POST)
# d)Modificar un préstamo por su ID (PUT)
# e)Eliminar un préstamo por su ID (DELETE)

from flask import Blueprint, request, jsonify
from modelos.entidades.classPrestamo import Prestamo
from modelos.repositorios.repoPrestamo import RepositorioPrestamo

# Crear un blueprint
prestamos_bp = Blueprint('prestamos_bp', __name__)

# Crear un repositorio
repositorio_prestamos = RepositorioPrestamo()

# a) Consultar todos los préstamos
@prestamos_bp.route('/prestamos', methods=['GET'])
def obtenerPrestamos():
    try:
        prestamos = repositorio_prestamos.obtenerTodos()
        return jsonify([prestamo.toDiccionario() for prestamo in prestamos])
    except:
        return jsonify({'mensaje': 'Error al obtener los préstamos'}), 500

# b) Buscar préstamo por socio DNI y libro ISBN
@prestamos_bp.route('/prestamos/<int:dni>/<int:isbn>', methods=['GET'])
def buscarPrestamo(dni, isbn):
    try:
        prestamo = repositorio_prestamos.buscar(dni, isbn)
        if prestamo is not None:
            return jsonify(prestamo.toDiccionario())
        return jsonify({'mensaje': 'Préstamo no encontrado'}), 404
    except:
        return jsonify({'mensaje': 'Error al buscar el préstamo'}), 500

# c) Agregar un nuevo préstamo
@prestamos_bp.route('/prestamos', methods=['POST'])
def agregarPrestamo():
    try:
        datos = request.json
        nuevoPrestamo = Prestamo.fromDiccionario(datos)
        repositorio_prestamos.agregar(nuevoPrestamo)
        return jsonify({'mensaje': 'Préstamo agregado correctamente'})
    except ValueError as e:
        return jsonify({'mensaje': str(e)}), 400

# d) Modificar un préstamo por su ID
@prestamos_bp.route('/prestamos/<int:id>', methods=['PUT'])
def modificarPrestamo(id):
    try:
        datos = request.json
        prestamo = Prestamo(
            datos['dni'], 
            datos['isbn'], 
            datos['fecha_prestamo'], 
            datos['fecha_devolucion']
            )
        repositorio_prestamos.modificar(id, prestamo)
        return jsonify({'mensaje': 'Préstamo modificado correctamente'})
    except:
        return jsonify({'mensaje': 'Error al modificar el préstamo'}), 500

# e) Eliminar un préstamo por su ID
@prestamos_bp.route('/prestamos/<int:id>', methods=['DELETE'])
def eliminarPrestamo(id):
    try:
        repositorio_prestamos.eliminarPorID(id)
        return jsonify({'mensaje': 'Préstamo eliminado correctamente'}), 200
    except ValueError as e:
        return jsonify({'mensaje': str(e)}), 400
    except:
        return jsonify({'mensaje': 'Error al eliminar el préstamo'}), 500

