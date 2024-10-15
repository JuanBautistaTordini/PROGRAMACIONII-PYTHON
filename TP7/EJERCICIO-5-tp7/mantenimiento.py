# mantenimiento.py

'''Clase: Mantenimiento (hereda de Persona)
Atributos:
legajo: str
area: str
Métodos:
__init__(self, nombre: str, apellido: str, dni: str, legajo: str, area: str)'''

from persona import Persona

class Mantenimiento(Persona):
    def __init__(self, nombre: str, apellido: str, dni: str, legajo: str, area: str):
        super().__init__(nombre, apellido, dni)  # Se eliminó 'self'
        self.__legajo = legajo
        self.__area = area
        
    def get_legajo(self):
        return self.__legajo
    
    def set_legajo(self, legajo: str):
        self.__legajo = legajo
        
    def get_area(self):
        return self.__area
    
    def set_area(self, area: str):
        self.__area = area
    
    def __str__(self):
        return f"Legajo: {self.__legajo}, Area: {self.__area}"