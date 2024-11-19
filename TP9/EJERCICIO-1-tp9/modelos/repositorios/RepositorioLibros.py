'''
+------------------------+
| RepositorioLibros      |
+------------------------+
| - libros: list<Libro>  |
+------------------------+
| + RepositorioLibro()   |
| - cargarTodos()        |
| - guardarTodos()       |
| + obtenerTodos(): list<Libro> |
| + existe(libto:Libro): bool |
| + existeISBN(isbn:int): bool |
| + agregar(nuevoLibro:Libro) |
| + modificarPorISBN(isbn:int, titulo: str, autor: str, genero: str, anio_publicacion: int)|
| + eliminarPorISBN(isbn:int) |
+------------------------+

observaciones:
Al agregar un nuevo libro no se debe duplicar la información 
existente, por lo tanto, hay que verificar que el libro 
no exista antes de agregarlo

'''

from modelos.entidades.Libro import Libro
import json

class RepositorioLibros:
    def __init__(self):
        self.libros = []
        self.cargarTodos()
    
    def cargarTodos(self):
        try:
            with open('./libros.json', 'r', encoding='utf-8') as archivo:
                libros = json.load(archivo)
                for libro in libros:
                    self.libros.append(Libro.fromDiccionario(libro))
        except FileNotFoundError:
            return []
            
    
    def guardarTodos(self):
        with open('./libros.json', 'w') as archivo:
            libros = [libro.toDiccionario() for libro in self.libros]
            json.dump(libros, archivo)
    
    def obtenerTodos(self):
        return self.libros
    
    def existe(self, libro:Libro):
        return libro in self.libros
    
    def existeISBN(self, isbn:int):
        return any(libro.isbn == isbn for libro in self.libros)
    
    def agregar(self, nuevoLibro:Libro):
        if not self.existe(nuevoLibro):
            self.libros.append(nuevoLibro)
            self.guardarTodos()
    
    def modificarPorISBN(self, isbn:int, titulo:str, autor:str, genero:str, anio_publicacion:int):
        for libro in self.libros:
            if libro.isbn == isbn:
                libro.titulo = titulo
                libro.autor = autor
                libro.genero = genero
                libro.anio_publicacion = anio_publicacion
                self.guardarTodos()
                break
    
    def eliminarPorISBN(self, isbn:int):
        for libro in self.libros:
            if libro.isbn == isbn:
                self.libros.remove(libro)
                self.guardarTodos()
                break
    
    def __str__(self):
        return f'RepositorioLibros({self.libros})'