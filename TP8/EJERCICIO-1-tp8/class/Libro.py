import json

class Libro:
    def __init__(self, titulo: str, autor: str, genero: str, ano_publicacion: int, isbn: int):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__ano_publicacion = ano_publicacion
        self.__isbn = isbn
    
    def toDiccionario(self):
        return {
            "Título": self.__titulo,
            "Autor": self.__autor,
            "Género": self.__genero,
            "Año de Publicación": self.__ano_publicacion,
            "ISBN": self.__isbn,
        }
    
    @classmethod
    def fromDiccionario(cls, dicc):
        return cls(
            dicc["Título"],
            dicc["Autor"],
            dicc["Género"],
            dicc["Año de Publicación"],
            dicc["ISBN"],
        )