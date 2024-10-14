# quinta.py

from inmueble import Inmueble

class Quinta(Inmueble):
    def __init__(self, codigo: int, domicilio: str, propietario: str, metrosCuadrados: int, estado: int, metrosParque: int):
        super().__init__(codigo, domicilio, propietario, metrosCuadrados, estado)
        self.__metrosParque = metrosParque

    def costoAlquiler(self, base: int) -> float:
        costo_base = super().costoAlquiler(base)
        return costo_base + (500 * (self.__metrosParque // 15))

    def precioVenta(self, m2: float) -> float:
        precio_base = super().precioVenta(m2)
        return precio_base + (0.5 * m2 * self.__metrosParque)

    def get_metrosParque(self) -> int:
        return self.__metrosParque

    def set_metrosParque(self, metrosParque: int) -> None:
        self.__metrosParque = metrosParque

    def get_codigo(self) -> int:
        return self._Inmueble__codigo

    def set_codigo(self, codigo: int) -> None:
        self._Inmueble__codigo = codigo

    def get_domicilio(self) -> str:
        return self._Inmueble__domicilio

    def set_domicilio(self, domicilio: str) -> None:
        self._Inmueble__domicilio = domicilio

    def get_propietario(self) -> str:
        return self._Inmueble__propietario

    def set_propietario(self, propietario: str) -> None:
        self._Inmueble__propietario = propietario

    def get_estado(self) -> int:
        return self._Inmueble__estado

    def set_estado(self, estado: int) -> None:
        self._Inmueble__estado = estado