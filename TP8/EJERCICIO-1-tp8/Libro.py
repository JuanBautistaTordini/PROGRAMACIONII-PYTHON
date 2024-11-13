import json

class Libro:
    # Constructor de la clase Libro
    def __init__(self, titulo: str, autor: str, genero: str, ano_publicacion: int, isbn: int):
        # Inicializa los atributos privados de la clase
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__ano_publicacion = ano_publicacion
        self.__isbn = isbn
    
    # Método para convertir el objeto Libro a un diccionario
    def toDiccionario(self):
        return {
            "Título": self.__titulo,
            "Autor": self.__autor,
            "Género": self.__genero,
            "Año de Publicación": self.__ano_publicacion,
            "ISBN": self.__isbn,
        }
    
    # Método de clase para crear un objeto Libro a partir de un diccionario
    @classmethod
    def fromDiccionario(cls, dicc):
        return cls(
            dicc["Título"],
            dicc["Autor"],
            dicc["Género"],
            dicc["Año de Publicación"],
            dicc["ISBN"],
        )