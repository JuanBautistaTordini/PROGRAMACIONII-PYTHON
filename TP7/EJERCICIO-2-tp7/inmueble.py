# inmueble.py
 
# Diagrama de la clase Inmueble:
#
# +-------------------+
# |     Inmueble      |
# +-------------------+
# | - __codigo: int   |
# | - __domicilio: str|
# | - __propietario: str|
# | - __metrosCuadrados: int|
# | - __estado: int   |
# +-------------------+
# | + __init__(codigo: int, domicilio: str, propietario: str, metrosCuadrados: int, estado: int) |
# | + get_codigo() -> int |
# | + get_domicilio() -> str |
# | + get_propietario() -> str |
# | + get_metrosCuadrados() -> int |
# | + get_estado() -> int |
# | + set_domicilio(domicilio: str) |
# | + set_propietario(propietario: str) |
# | + set_metrosCuadrados(metros: int) |
# | + set_estado(estado: int) |
# | + costoAlquiler(base: int) -> float |
# | + precioVenta(m2: float) -> float |
# +-------------------+

class Inmueble:
    def __init__(self, codigo: int, domicilio: str, propietario: str, metrosCuadrados: int, estado: int):
        self.__codigo = codigo
        self.__domicilio = domicilio
        self.__propietario = propietario
        self.__metrosCuadrados = metrosCuadrados
        self.__estado = estado

    def get_codigo(self) -> int:
        return self.__codigo

    def get_domicilio(self) -> str:
        return self.__domicilio

    def set_domicilio(self, domicilio: str) -> None:
        if isinstance(domicilio, str) and domicilio.strip():
            self.__domicilio = domicilio
        else:
            raise ValueError("El domicilio debe ser una cadena no vacía")

    def get_propietario(self) -> str:
        return self.__propietario

    def set_propietario(self, propietario: str) -> None:
        if isinstance(propietario, str) and propietario.strip():
            self.__propietario = propietario
        else:
            raise ValueError("El propietario debe ser una cadena no vacía")

    def get_metrosCuadrados(self) -> int:
        return self.__metrosCuadrados

    def set_metrosCuadrados(self, metros: int) -> None:
        if isinstance(metros, int) and metros > 0:
            self.__metrosCuadrados = metros
        else:
            raise ValueError("Los metros cuadrados deben ser un número entero positivo")

    def get_estado(self) -> int:
        return self.__estado

    def set_estado(self, estado: int) -> None:
        if isinstance(estado, int) and 0 <= estado <= 3:
            self.__estado = estado
        else:
            raise ValueError("El estado debe ser un número entero entre 0 y 3")

    def costoAlquiler(self, base: int) -> float:
        return base * self.__metrosCuadrados * 0.1

    def precioVenta(self, m2: float) -> float:
        return m2 * self.__metrosCuadrados * 1.5