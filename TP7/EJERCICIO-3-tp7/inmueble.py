# inmueble.py

class Inmueble:
    def __init__(self, codigo: int, domicilio: str, propietario: str, metrosCuadrados: int, estado: int):
        self.__codigo = codigo
        self.__domicilio = domicilio
        self.__propietario = propietario
        self.__metrosCuadrados = metrosCuadrados
        self.__estado = estado

    def costoAlquiler(self, base: int) -> float:
        return base + (100 * self.__metrosCuadrados)

    def precioVenta(self, m2: float) -> float:
        return m2 * self.__metrosCuadrados

    def get_metrosCuadrados(self) -> int:
        return self.__metrosCuadrados

    def set_metrosCuadrados(self, metrosCuadrados: int) -> None:
        self.__metrosCuadrados = metrosCuadrados

    def get_codigo(self) -> int:
        return self.__codigo

    def set_codigo(self, codigo: int) -> None:
        self.__codigo = codigo

    def get_domicilio(self) -> str:
        return self.__domicilio

    def set_domicilio(self, domicilio: str) -> None:
        self.__domicilio = domicilio

    def get_propietario(self) -> str:
        return self.__propietario

    def set_propietario(self, propietario: str) -> None:
        self.__propietario = propietario

    def get_estado(self) -> int:
        return self.__estado

    def set_estado(self, estado: int) -> None:
        self.__estado = estado