# 8) Un organizador de eventos nos pide diseñar un sistema simple para gestionar los 
# eventos. El sistema debe permitir registrar eventos, participantes y organizadores, y 
# asignar participantes a eventos y organizadores a eventos. 
# Requerimientos 

# Evento: Cada evento tiene un nombre, una fecha y una descripción. Los eventos 
# pueden tener múltiples participantes y un organizador asignado. 

# Participante: Cada participante tiene un nombre, una dirección de correo electrónico 
# y un número de teléfono. Los participantes pueden registrarse en uno o más 
# eventos. 

# Organizador: Cada organizador tiene un nombre, una dirección de correo electrónico 
# y una especialidad (por ejemplo, planificación de eventos, catering, músico, DJ, etc.). 
# Cada organizador puede estar a cargo de uno o más eventos. 


# A. Crea un diagrama de clases que incluya tres clases principales: Evento, 
# Participante y Organizador. 
# B. Implementa las clases en python 
# C.  Crea una clase tester para cada clase implementada


# Clase Evento:

#     Atributos:
#         nombre: Nombre del evento (string).
#         fecha: Fecha del evento (datetime).
#         descripcion: Descripción del evento (string).
#         participantes: Lista de participantes asignados al evento.
#         organizador: Organizador asignado al evento (puede ser None inicialmente).
#     Métodos:
#     asignar_organizador(organizador): Asigna un organizador al evento.
#     agregar_participante(participante): Agrega un participante al evento.

class Evento:
    def __init__(self, nombre: str, fecha: str, descripcion: str):
        if not nombre:
            raise ValueError("El nombre del evento no puede estar vacío.")
        if not fecha:
            raise ValueError("La fecha del evento no puede estar vacía.")
        if not descripcion:
            raise ValueError("La descripción del evento no puede estar vacía.")
        
        self.__nombre = nombre
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__participantes = []
        self.__organizador = None 
    
    #metodos getter y setter
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre: str):
        if not nombre:
            raise ValueError("El nombre del evento no puede estar vacío.")
        self.__nombre = nombre
    
    def get_fecha(self):
        return self.__fecha
    
    def set_fecha(self, fecha: str):
        if not fecha:
            raise ValueError("La fecha del evento no puede estar vacía.")
        self.__fecha = fecha
    
    def get_descripcion(self):
        return self.__descripcion
    
    def set_descripcion(self, descripcion: str):
        if not descripcion:
            raise ValueError("La descripción del evento no puede estar vacía.")
        self.__descripcion = descripcion
    
    def get_participantes(self):
        return self.__participantes
    
    def set_participantes(self, participantes: list):
        self.__participantes = participantes
    
    def get_organizador(self):
        return self.__organizador
    
    def set_organizador(self, organizador):
        self.__organizador = organizador
    
    def asignar_organizador(self, organizador):
        if not isinstance(organizador, Organizador):
            raise TypeError("El organizador debe ser una instancia de la clase Organizador.")
        self.__organizador = organizador
    
    def agregar_participante(self, participante):
        if not isinstance(participante, Participante):
            raise TypeError("El participante debe ser una instancia de la clase Participante.")
        self.__participantes.append(participante)
    
    def __str__(self):
        organizador_str = self.__organizador.get_nombre() if self.__organizador else "Ninguno"
        participantes_nombres = [participante.get_nombre() for participante in self.__participantes]
        participantes_str = ', '.join(participantes_nombres) if participantes_nombres else "Ninguno"
        
        return (f"Evento: {self.__nombre}\n"
                f"Fecha: {self.__fecha}\n"
                f"Descripción: {self.__descripcion}\n"
                f"Organizador: {organizador_str}\n"
                f"Participantes: {participantes_str}")
        