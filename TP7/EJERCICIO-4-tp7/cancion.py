# cancion.py

# Diagrama de clase Canción:

# - codigo: int
# - nombre: str
# - duracion: int
# - genero: str

# Métodos:
# - get_codigo(): int
# - set_codigo(codigo: int): void
# - get_nombre(): str
# - set_nombre(nombre: str): void
# - get_duracion(): int
# - set_duracion(duracion: int): void
# - get_genero(): str
# - set_genero(genero: str): void
# - reproducir(): void

# Clase Canción
class Cancion:
    def __init__(self, codigo, nombre, duracion, genero):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__duracion = duracion
        self.__genero = genero

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        if isinstance(codigo, int) and codigo > 0:
            self.__codigo = codigo
        else:
            raise ValueError("El código debe ser un número entero positivo.")

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self.__nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía.")

    def get_duracion(self):
        return self.__duracion

    def set_duracion(self, duracion):
        if isinstance(duracion, int) and duracion > 0:
            self.__duracion = duracion
        else:
            raise ValueError("La duración debe ser un número entero positivo.")

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        if isinstance(genero, str) and genero.strip():
            self.__genero = genero
        else:
            raise ValueError("El género debe ser una cadena no vacía.")

    def reproducir(self):
        print(f'Reproduciendo: {self.__nombre} - {self.__artista} - {self.__duracion} minutos - {self.__genero}')