# departamento.py

# Diagrama de la clase Departamento:

# Atributos de instancia:
# - gastosComunes: real (float)
#   Representa los gastos comunes asociados al departamento.
# - cochera: booleano (bool)
#   Indica si el departamento tiene cochera o no.

# Constructor:
# Se infiere que el constructor debe inicializar estos atributos,
# además de los heredados de la clase Inmueble.

# Comandos:
# No se especifican comandos adicionales en el diagrama,
# pero se podrían incluir métodos para modificar los atributos.

# Consultas:
# + costoAlquiler(base: entero): real
#   Calcula el costo de alquiler del departamento.
# + precioVenta(m2: real): real
#   Calcula el precio de venta del departamento.

# Nota: La clase Departamento hereda de otra clase (probablemente Inmueble),
# como se indica por la flecha de herencia en la parte superior del diagrama.

# Importación de la clase Inmueble
from inmueble import Inmueble

# Definición de la clase Departamento
class Departamento(Inmueble):
    def __init__(self, codigo: int, domicilio: str, propietario: str, metrosCuadrados: int, estado: int, gastosComunes: float, cochera: bool):
        super().__init__(codigo, domicilio, propietario, metrosCuadrados, estado)
        self.__gastosComunes = gastosComunes
        self.__cochera = cochera

    def costoAlquiler(self, base: int) -> float:
        return base + self.__gastosComunes
    
    def precioVenta(self, m2: float) -> float:
        return m2 * self.get_metrosCuadrados()
    
    def get_gastosComunes(self) -> float:
        return self.__gastosComunes
    
    def set_gastosComunes(self, gastosComunes: float) -> None:
        self.__gastosComunes = gastosComunes
    
    def get_cochera(self) -> bool:
        return self.__cochera
    
    def set_cochera(self, cochera: bool) -> None:
        self.__cochera = cochera
    


