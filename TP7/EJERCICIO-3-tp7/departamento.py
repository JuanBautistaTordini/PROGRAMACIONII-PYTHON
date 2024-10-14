# departamento.py

from inmueble import Inmueble

class Departamento(Inmueble):
    def __init__(self, codigo: int, domicilio: str, propietario: str, metrosCuadrados: int, estado: int, gastosComunes: float, cochera: bool):
        super().__init__(codigo, domicilio, propietario, metrosCuadrados, estado)
        self.__gastosComunes = gastosComunes
        self.__cochera = cochera

    def costoAlquiler(self, base: int) -> float:
        costo_base = super().costoAlquiler(base)
        return costo_base + (2000 if self.__cochera else 0)

    def precioVenta(self, m2: float) -> float:
        precio_base = super().precioVenta(m2)
        return precio_base + (3 * m2 if self.__cochera else 0)

    def get_gastosComunes(self) -> float:
        return self.__gastosComunes

    def set_gastosComunes(self, gastosComunes: float) -> None:
        self.__gastosComunes = gastosComunes

    def get_cochera(self) -> bool:
        return self.__cochera

    def set_cochera(self, cochera: bool) -> None:
        self.__cochera = cochera

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