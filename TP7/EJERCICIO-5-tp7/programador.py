# programador.py

'''Clase: Programador (hereda de Persona)
Atributos:
legajo: str
proyecto: str
Métodos:
__init__(self, nombre: str, apellido: str, dni: str, legajo: str, proyecto: str)
'''

from persona import Persona

class Programador(Persona):
    def __init__(self, nombre: str, apellido: str, dni: str, legajo: str, proyecto: str):
        super().__init__(nombre, apellido, dni)  # Se eliminó 'self'
        self.__legajo = legajo
        self.__proyecto = proyecto
        
    def get_legajo(self):
        return self.__legajo
    
    def set_legajo(self, legajo: str):
        self.__legajo = legajo
        
    def get_proyecto(self):
        return self.__proyecto
    
    def set_proyecto(self, proyecto: str):
        self.__proyecto = proyecto
    
    def __str__(self):
        return f"Legajo: {self.__legajo}, Proyecto: {self.__proyecto}"
    
    
