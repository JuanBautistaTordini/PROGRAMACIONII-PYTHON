# administrativo.py

''' Clase: Administrativo (hereda de Persona)
Atributos:
legajo: str
posicion: str
Métodos:
__init__(self, nombre: str, apellido: str, dni: str, legajo: str, posicion: str)
'''

from persona import Persona

class Administrativo(Persona):
    def __init__(self, nombre: str, apellido: str, dni: str, legajo: str, posicion: str):
        super().__init__(nombre, apellido, dni)  # Se eliminó 'self'
        self.__legajo = legajo
        self.__posicion = posicion

    def get_legajo(self):
        return self.__legajo
    
    def set_legajo(self, legajo: str):
        self.__legajo = legajo
        
    def get_posicion(self):
        return self.__posicion
    
    def set_posicion(self, posicion: str):
        self.__posicion = posicion
    
    def __str__(self):
        return f"Legajo: {self.__legajo}, Posicion: {self.__posicion}"
    
    
