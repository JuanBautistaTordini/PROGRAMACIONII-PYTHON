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
        self._marca = marca
        self._modelo = modelo
        self._patente = patente
        self._color = color
        self._anio_fabricacion = anio_fabricacion
        self._precio = precio
        self._kilometraje = kilometraje
        self._tipo_combustible = tipo_combustible
    
    ## getters y setters para cada atributo
    def get_marca(self):
        return self._marca
    
    def set_marca(self, marca: str):
        self._marca = marca
        
    def get_modelo(self):
        return self._modelo
    
    def set_modelo(self, modelo: str):
        self._modelo = modelo
    
    def get_patente(self):
        return self._patente
    
    def set_patente(self, patente: str):
        self._patente = patente
    
    def get_color(self):
        return self._color
    
    def set_color(self, color: str):
        self._color = color
    
    def get_anio_fabricacion(self):
        return self._anio_fabricacion
    
    def set_anio_fabricacion(self, anio_fabricacion: int):
        self._anio_fabricacion = anio_fabricacion
    
    def get_precio(self):
        return self._precio
    
    def set_precio(self, precio: float):
        self._precio = precio
    
    def get_kilometraje(self):
        return self._kilometraje
    
    def set_kilometraje(self, kilometraje: float):
        self._kilometraje = kilometraje
    
    def get_tipo_combustible(self):
        return self._tipo_combustible
    
    def set_tipo_combustible(self, tipo_combustible: str):
        self._tipo_combustible = tipo_combustible
    
    # Metodos:
    def __str__(self):
        return f"Vehiculo: {self._marca} {self._modelo}, Patente: {self._patente}, Color: {self._color}, Año de fabricación: {self._anio_fabricacion}, Precio: {self._precio}, Kilometraje: {self._kilometraje}, Tipo de combustible: {self._tipo_combustible}"
        
