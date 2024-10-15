# auto.py

# 2. Clase Auto (hereda de Vehiculo):
#    - Atributos adicionales:
#      - cantidad_puertas: int
#      - tiene_aire_acondicionado: bool
#    - Métodos:
#      - __init__(self, marca, modelo, patente, color, anio_fabricacion, precio, kilometraje, tipo_combustible, cantidad_puertas, tiene_aire_acondicionado)
#      - getters y setters para los atributos adicionales
#      - __str__(self)

from vehiculos import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca: str, modelo: str, patente: str, color: str, anio_fabricacion: int, precio: float, kilometraje: float, tipo_combustible: str, cantidad_puertas: int, tiene_aire_acondicionado: bool):
        super().__init__(marca, modelo, patente, color, anio_fabricacion, precio, kilometraje, tipo_combustible)
        self.__cantidad_puertas = cantidad_puertas
        self.__tiene_aire_acondicionado = tiene_aire_acondicionado
    
    # getters y setters para los atributos adicionales
    
    def get_cantidad_puertas(self):
        return self.__cantidad_puertas
    
    def set_cantidad_puertas(self, cantidad_puertas: int):
        self.__cantidad_puertas = cantidad_puertas
    
    def get_tiene_aire_acondicionado(self):
        return self.__tiene_aire_acondicionado
    
    def set_tiene_aire_acondicionado(self, tiene_aire_acondicionado: bool):
        self.__tiene_aire_acondicionado = tiene_aire_acondicionado
    
    def __str__(self):
        return f"Auto: {self.get_marca()} {self.get_modelo()}, Patente: {self.get_patente()}, Color: {self.get_color()}, Año de fabricación: {self.get_anio_fabricacion()}, Precio: {self.get_precio()}, Kilometraje: {self.get_kilometraje()}, Tipo de combustible: {self.get_tipo_combustible()}, Cantidad de puertas: {self.__cantidad_puertas}, Tiene aire acondicionado: {self.__tiene_aire_acondicionado}"

