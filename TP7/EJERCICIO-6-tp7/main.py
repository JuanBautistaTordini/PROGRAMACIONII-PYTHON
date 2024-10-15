'''Una concesionaria de automóviles vende una gran variedad de vehículos. Cada 
vehículo tiene una marca, modelo, patente, color, año de fabricación, precio y un 
determinado kilometraje. Además, se registra el tipo de combustible que utiliza 
(nafta, diésel o eléctrico). Los autos, además de las características generales de un 
vehículo, tienen una cantidad específica de puertas y algunos cuentan con aire 
acondicionado. Por otro lado, las motos tienen un ancho de manubrio y una 
cilindrada particular. 
a. Realizar el diagrama de clases en UML  
b. Implementar las clases en python. '''

# Diagrama de clases por ítems:

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

# 2. Clase Auto (hereda de Vehiculo):
#    - Atributos adicionales:
#      - cantidad_puertas: int
#      - tiene_aire_acondicionado: bool
#    - Métodos:
#      - __init__(self, marca, modelo, patente, color, anio_fabricacion, precio, kilometraje, tipo_combustible, cantidad_puertas, tiene_aire_acondicionado)
#      - getters y setters para los atributos adicionales
#      - __str__(self)

# 3. Clase Moto (hereda de Vehiculo):
#    - Atributos adicionales:
#      - ancho_manubrio: float
#      - cilindrada: int
#    - Métodos:
#      - __init__(self, marca, modelo, patente, color, anio_fabricacion, precio, kilometraje, tipo_combustible, ancho_manubrio, cilindrada)
#      - getters y setters para los atributos adicionales
#      - __str__(self)

# Importaciones:

from vehiculos import Vehiculo
from auto import Auto
from moto import Moto

# Tester:

if __name__ == "__main__":
    # Crear una instancia de Vehiculo
    vehiculo = Vehiculo("Toyota", "Corolla", "ABC123", "Rojo", 2020, 20000.0, 15000.0, "Gasolina")
    print(vehiculo)

    # Crear una instancia de Auto
    auto = Auto("Ford", "Fiesta", "XYZ789", "Azul", 2019, 15000.0, 12000.0, "Gasolina", 5, True)
    print(auto)

    # Crear una instancia de Moto
    moto = Moto("Yamaha", "MT-07", "MOTO123", "Negro", 2021, 8000.0, 5000.0, "Gasolina", 0.8, 689)
    print(moto)

