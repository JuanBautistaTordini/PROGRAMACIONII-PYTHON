# playlist.py

# Diagrama de la clase Playlist:

#Constructor:
# - codigo: int
# - nombre: str
# - canciones: list

# Métodos:
# - agregarCancion(cancion): void
# - eliminarCancion(cancion): void
# - get_codigo(): int
# - set_codigo(codigo: int): void
# - get_nombre(): str
# - set_nombre(nombre: str): void
# - get_canciones(): list

# Clase Playlist
class Playlist:
    def __init__(self, codigo: int, nombre: str):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__canciones = []

    def agregarCancion(self, cancion) -> None:
        self.__canciones.append(cancion)

    def eliminarCancion(self, cancion) -> None:
        self.__canciones.remove(cancion)

    def get_codigo(self) -> int:
        return self.__codigo

    def set_codigo(self, codigo: int) -> None:
        if isinstance(codigo, int) and codigo > 0:
            self.__codigo = codigo
        else:
            raise ValueError("El código debe ser un número entero positivo.")

    def get_nombre(self) -> str:
        return self.__nombre

    def set_nombre(self, nombre: str) -> None:
        if isinstance(nombre, str) and nombre.strip():
            self.__nombre = nombre
        else:
            raise ValueError("El nombre no puede estar vacío.")

    def get_canciones(self) -> list:
        return self.__canciones.copy()