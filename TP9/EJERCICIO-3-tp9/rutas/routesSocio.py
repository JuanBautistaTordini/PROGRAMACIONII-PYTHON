# El servicio deberá proveer endpoints (rutas) para: 
# a) consultar todos los socios registrados (GET) 
# b) buscar un socio en particular por número de DNI (GET) 
# c) agregar un nuevo socio (POST) 
# d) modificar los datos de un socio por su DNI(PUT) 
# e) eliminar un socio del sistema dado su DNI (DELETE). 

from flask import Blueprint, request, jsonify
from datetime import datetime
from modelos.entidades.classSocio import Socio
from modelos.repositorios.repoSocios import RepoSocios

# Crear un blueprint
socios_bp = Blueprint('socios_bp', __name__)

# Crear un repositorio
repositorio = RepoSocios()

# a) consultar todos los socios registrados (GET)
@socios_bp.route('/socios', methods=['GET'])

def obtenerSocios():
    try:
        socios = repositorio.obtenerTodos()
        return jsonify([socio.toDiccionario() for socio in socios])
    except:
        return jsonify({'mensaje': 'Error al obtener los socios'}), 500

# b) buscar un socio en particular por número de DNI (GET)
@socios_bp.route('/socios/<int:dni>', methods=['GET'])

def obtenerSocio(dni):
    try: 
        for socio in repositorio.obtenerTodos():
            if socio.getDni() == dni:
                return jsonify(socio.toDiccionario())
        return jsonify({'mensaje': 'Socio no encontrado'}), 404
    except:
        return jsonify({'mensaje': 'Error al obtener el socio'}), 500
    
# c) agregar un nuevo socio (POST)
@socios_bp.route('/socios', methods=['POST'])

def agregarSocio():
    try:
        datos = request.json
        nuevoSocio = Socio.fromDiccionario(datos)
        repositorio.agregar(nuevoSocio)
        return jsonify({'mensaje': 'Socio agregado correctamente'})
    except ValueError as e:
        return jsonify({'mensaje': str(e)}), 400
    except:
        return jsonify({'mensaje': 'Error al agregar el socio'}), 500

# d) modificar los datos de un socio por su DNI(PUT)
@socios_bp.route('/socios/<int:dni>', methods=['PUT'])

def modificarSocio(dni):
    try:
        datos = request.json
        repositorio.modificarPorDNI(
            dni,
            datos['nombre'],
            datos['apellido'],
            datos['mail'],
            datos['fecha_nacimiento']
        )
        return jsonify({'mensaje': 'Socio modificado correctamente'})
    except ValueError as e:
        return jsonify({'mensaje': str(e)}), 400
    except:
        return jsonify({'mensaje': 'Error al modificar el socio'}), 500

# e) eliminar un socio del sistema dado su DNI (DELETE)
@socios_bp.route('/socios/<int:dni>', methods=['DELETE'])

def eliminarSocio(dni):
    try:
        repositorio.eliminarPorDNI(dni)
        return jsonify({'mensaje': 'Socio eliminado correctamente'})
    except ValueError as e:
        return jsonify({'mensaje': str(e)}), 400
    except:
        return jsonify({'mensaje': 'Error al eliminar el socio'}), 500
    
