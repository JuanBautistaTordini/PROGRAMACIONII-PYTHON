# dispositivo.py
class Dispositivo:
    def __init__(self, id, nombre, tipo):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo

    def get_id(self):
        return self.__id

    def set_id(self, id):
        if isinstance(id, int) and id > 0:
            self.__id = id
        else:
            raise ValueError("El ID debe ser un número entero positivo.")

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self.__nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía.")

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        if isinstance(tipo, str) and tipo.strip():
            self.__tipo = tipo
        else:
            raise ValueError("El tipo debe ser una cadena no vacía.")