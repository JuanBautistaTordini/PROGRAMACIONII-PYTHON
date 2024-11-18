# El servicio deberá proveer endpoints (rutas) para: 
# a) consultar todos los libros registrados (GET) 
# b) buscar un libro en particular por ISBN (GET) 
# c) agregar un nuevo libro (POST) 
# d) modificar los datos de un libro ingresando su ISBN (PUT) 
# e) eliminar un libro del sistema dado su ISBN (DELETE) 

from flask import Blueprint, jsonify, request
from modelos.entidades.Libro import Libro
from modelos.repositorios.RepositorioLibros import RepositorioLibros

#objeto de tipo Blueprint
libros_bp = Blueprint('libros', __name__)

#repositorio de libros
repositorio = RepositorioLibros()

''' ENDPOINTS '''
# a) consultar todos los libros registrados (GET)
@libros_bp.route('/libros', methods=['GET'])
def obtenerTodos():
    libros = repositorio.obtenerTodos()
    return jsonify([libro.toDiccionario() for libro in libros])

# b) buscar un libro en particular por ISBN (GET)
@libros_bp.route('/libros/<int:isbn>', methods=['GET'])
def buscarPorISBN(isbn):
    for libro in repositorio.obtenerTodos():
        if libro.getISBN() == isbn:
            return jsonify(libro.toDiccionario())
    return jsonify({'mensaje': 'Libro no encontrado'}), 404

# c) agregar un nuevo libro (POST)
@libros_bp.route('/libros', methods=['POST'])
def agregarLibro():
    try:
        datos = request.json
        isbn = datos['isbn']
        titulo = datos['titulo']
        autor = datos['autor']
        genero = datos['genero']
        anio_publicacion = datos['anio_publicacion']
        
        # Verificar si el libro con el mismo ISBN ya existe
        if repositorio.existeISBN(isbn):
            return jsonify({'mensaje': 'El libro con este ISBN ya existe'}), 409
        
        # Crear el nuevo libro si no existe
        nuevoLibro = Libro(isbn, titulo, autor, genero, anio_publicacion)
        repositorio.agregar(nuevoLibro)
        return jsonify({'mensaje': 'Libro agregado'}), 201
    except ValueError as e:
        return jsonify({'mensaje': str(e)}), 400


# d) modificar los datos de un libro ingresando su ISBN (PUT)
@libros_bp.route('/libros/<int:isbn>', methods=['PUT'])
def modificarLibro(isbn):
    try:
        datos = request.json
        titulo = datos['titulo']
        autor = datos['autor']
        genero = datos['genero']
        anio_publicacion = datos['anio_publicacion']
        
        # Verificar si el libro con el ISBN existe
        libro = None
        for l in repositorio.obtenerTodos():
            if l.getISBN() == isbn:
                libro = l
                break
        
        if libro is None:
            return jsonify({'mensaje': 'Libro no encontrado'}), 404
        
        # Si el libro existe, modificar los datos
        repositorio.modificarPorISBN(isbn, titulo, autor, genero, anio_publicacion)
        return jsonify({'mensaje': 'Libro modificado'}), 200
    
    except ValueError as e:
        return jsonify({'mensaje': str(e)}), 400

# e) eliminar un libro del sistema dado su ISBN (DELETE)
@libros_bp.route('/libros/<int:isbn>', methods=['DELETE'])
def eliminarLibro(isbn):
    try:
        # Verificar si el libro con el ISBN existe
        libro = None
        for l in repositorio.obtenerTodos():
            if l.getISBN() == isbn:
                libro = l
                break
        
        if libro is None:
            return jsonify({'mensaje': 'Libro no encontrado'}), 404
        
        # Si el libro existe, eliminarlo
        repositorio.eliminarPorISBN(isbn)
        return jsonify({'mensaje': 'Libro eliminado'}), 200
    
    except ValueError as e:
        return jsonify({'mensaje': str(e)}), 400


