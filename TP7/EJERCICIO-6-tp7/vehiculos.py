# vehiculos.py

# 1. Clase Vehiculo:
#    - Atributos:
#      - marca: str
#      - modelo: str
#      - patente: str
#      - color: str
#      - anio_fabricacion: int
#      - precio: float
#      - kilometraje: float
#      - tipo_combustible: str
#    - Métodos:
#      - __init__(self, marca, modelo, patente, color, anio_fabricacion, precio, kilometraje, tipo_combustible)
#      - getters y setters para cada atributo
#      - __str__(self)

class Vehiculo:
    def __init__(self, marca: str, modelo: str, patente: str, color: str, anio_fabricacion: int, precio: float, kilometraje: float, tipo_combustible: str):
        self.__marca = marca
        self.__modelo = modelo
        self.__patente = patente
        self.__color = color
        self.__anio_fabricacion = anio_fabricacion
        self.__precio = precio
        self.__kilometraje = kilometraje
        self.__tipo_combustible = tipo_combustible
    
    ## getters y setters para cada atributo
    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca: str):
        self.__marca = marca
        
    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self, modelo: str):
        self.__modelo = modelo
    
    def get_patente(self):
        return self.__patente
    
    def set_patente(self, patente: str):
        self.__patente = patente
    
    def get_color(self):
        return self.__color
    
    def set_color(self, color: str):
        self.__color = color
    
    def get_anio_fabricacion(self):
        return self.__anio_fabricacion
    
    def set_anio_fabricacion(self, anio_fabricacion: int):
        self.__anio_fabricacion = anio_fabricacion
    
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio: float):
        self.__precio = precio
    
    def get_kilometraje(self):
        return self.__kilometraje
    
    def set_kilometraje(self, kilometraje: float):
        self.__kilometraje = kilometraje
    
    def get_tipo_combustible(self):
        return self.__tipo_combustible
    
    def set_tipo_combustible(self, tipo_combustible: str):
        self.__tipo_combustible = tipo_combustible
    
    # Metodos:
    def __str__(self):
        return f"Vehiculo: {self.__marca} {self.__modelo}, Patente: {self.__patente}, Color: {self.__color}, Año de fabricación: {self.__anio_fabricacion}, Precio: {self.__precio}, Kilometraje: {self.__kilometraje}, Tipo de combustible: {self.__tipo_combustible}"
        
