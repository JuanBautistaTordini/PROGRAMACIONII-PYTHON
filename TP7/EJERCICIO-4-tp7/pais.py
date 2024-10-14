# pais.py
class Pais:
    def __init__(self, codigo, nombre, cantidadDispositivos):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__cantidadDispositivos = cantidadDispositivos

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        if isinstance(codigo, str) and len(codigo) > 0:
            self.__codigo = codigo
        else:
            raise ValueError("El código debe ser una cadena no vacía")

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str) and len(nombre) > 0:
            self.__nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía")

    def get_cantidadDispositivos(self):
        return self.__cantidadDispositivos

    def set_cantidadDispositivos(self, cantidadDispositivos):
        if isinstance(cantidadDispositivos, int) and cantidadDispositivos >= 0:
            self.__cantidadDispositivos = cantidadDispositivos
        else:
            raise ValueError("La cantidad de dispositivos debe ser un número entero no negativo")