# propietario.py

class Propietario:
    def __init__(self, nombre: str, dni: str):
        self.__nombre = nombre
        self.__dni = dni

    def toString(self) -> str:
        return f"Propietario: {self.__nombre}, DNI: {self.__dni}"

    def get_nombre(self) -> str:
        return self.__nombre

    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def get_dni(self) -> str:
        return self.__dni

    def set_dni(self, dni: str) -> None:
        self.__dni = dni