# moto.py

# 3. Clase Moto (hereda de Vehiculo):
#    - Atributos adicionales:
#      - ancho_manubrio: float
#      - cilindrada: int
#    - Métodos:
#      - __init__(self, marca, modelo, patente, color, anio_fabricacion, precio, kilometraje, tipo_combustible, ancho_manubrio, cilindrada)
#      - getters y setters para los atributos adicionales
#      - __str__(self)

from vehiculos import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str, patente: str, color: str, anio_fabricacion: int, precio: float, kilometraje: float, tipo_combustible: str, ancho_manubrio: float, cilindrada: int):
        super().__init__(marca, modelo, patente, color, anio_fabricacion, precio, kilometraje, tipo_combustible)
        self.__ancho_manubrio = ancho_manubrio
        self.__cilindrada = cilindrada
    
    ## getters y setters para los atributos adicionales
    
    def get_ancho_manubrio(self):
        return self.__ancho_manubrio
    
    def set_ancho_manubrio(self, ancho_manubrio: float):
        self.__ancho_manubrio = ancho_manubrio
    
    def get_cilindrada(self):
        return self.__cilindrada
    
    def set_cilindrada(self, cilindrada: int):
        self.__cilindrada = cilindrada
    
    def __str__(self):
        return f"Moto: {self.get_marca()} {self.get_modelo()}, Patente: {self.get_patente()}, Color: {self.get_color()}, Año de fabricación: {self.get_anio_fabricacion()}, Precio: {self.get_precio()}, Kilometraje: {self.get_kilometraje()}, Tipo de combustible: {self.get_tipo_combustible()}, Ancho de manubrio: {self.__ancho_manubrio}, Cilindrada: {self.__cilindrada}"
    
    
    
