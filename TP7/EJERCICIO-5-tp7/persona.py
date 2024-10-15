# persona.py

# Clase: Persona
# Atributos:
# nombre: str
# apellido: str
# dni: str
# Métodos:
# __init__(self, nombre: str, apellido: str, dni: str)

class Persona:
    #atributos de instancia privados:
    def __init__(self, nombre: str, apellido: str, dni: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni

    #metodos de instancia:
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre: str):
        self.__nombre = nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def set_apellido(self, apellido: str):
        self.__apellido = apellido
    
    def get_dni(self):
        return self.__dni
    
    def set_dni(self, dni: str):
        self.__dni = dni
    
    def __str__(self):
        return f"Nombre: {self.__nombre}, Apellido: {self.__apellido}, DNI: {self.__dni}"
    
    
        
