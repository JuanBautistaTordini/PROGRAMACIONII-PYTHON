# quinta.py

# Diagrama de la clase Quinta:

# - Herencia:
#   La clase Quinta hereda de otra clase (Inmueble)

# - Atributos de instancia:
#   - metrosParque: entero
#     Representa la cantidad de metros cuadrados del parque de la quinta

# - Constructor:
#   Se infiere que el constructor debe inicializar el atributo metrosParque,
#   además de los atributos heredados de la clase padre

# - Comandos:
#   No se especifican comandos adicionales en el diagrama

# - Consultas:
#   + costoAlquiler(base: entero): real
#     Calcula el costo de alquiler de la quinta
#   + precioVenta(m2: real): real
#     Calcula el precio de venta de la quinta

# Nota: La implementación específica de estos métodos no se proporciona en el diagrama

# Importación de la clase Inmueble
from inmueble import Inmueble

# Definición de la clase Quinta
class Quinta(Inmueble):
    def __init__(self, codigo: int, domicilio: str, propietario: str, metrosCuadrados: int, estado: int, metrosParque: int):
        super().__init__(codigo, domicilio, propietario, metrosCuadrados, estado)
        self.__metrosParque = metrosParque

    def costoAlquiler(self, base: int) -> float:
        return base + self.__metrosParque
    
    def precioVenta(self, m2: float) -> float:
        return m2 * self.get_metrosCuadrados()
    
    def get_metrosParque(self) -> int:
        return self.__metrosParque
    
    def set_metrosParque(self, metrosParque: int) -> None:
        self.__metrosParque = metrosParque


