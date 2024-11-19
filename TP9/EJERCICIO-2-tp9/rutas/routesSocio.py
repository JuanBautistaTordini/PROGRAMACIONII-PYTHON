# El servicio deberá proveer endpoints (rutas) para: 
# a) consultar todos los socios registrados (GET) 
# b) buscar un socio en particular por número de DNI (GET) 
# c) agregar un nuevo socio (POST) 
# d) modificar los datos de un socio por su DNI(PUT) 
# e) eliminar un socio del sistema dado su DNI (DELETE). 

from flask import Flask, request, jsonify
from datetime import datetime
from modelos.entidades.classSocio import Socio
from modelos.repositorios.repoSocios import RepoSocios

