'''
+------------------------+
| RepositorioLibros      |
+------------------------+
| - libros: list<Libro>   |
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
'''

