'''
Diagrama clase Libro:
+----------------------------------------+
|               Libro                    |
+----------------------------------------+
| - titulo: str                          |
| - autor: str                           |
| - genero: str                          |
| - ano_publicacion: int                 |
| - isbn: int                            |
+----------------------------------------+
| + get_titulo(): str                    |
| + get_autor(): str                     |
| + get_genero(): str                    |
| + get_ano_publicacion(): int           |
| + get_isbn(): int                      |
| + toDiccionario(): dict                |
| + fromDiccionario(dicc: dict): Libro   |
+----------------------------------------+

'''


class Libro:
    """
    Clase que representa un libro.

    Atributos:
    - titulo (str): El título del libro.
    - autor (str): El autor del libro.
    - genero (str): El género del libro.
    - ano_publicacion (int): El año de publicación del libro.
    - isbn (int): El número ISBN del libro.
    """

    def __init__(self, titulo: str, autor: str, genero: str, ano_publicacion: int, isbn: int):
        if not isinstance(titulo, str):
            raise ValueError("El título debe ser una cadena de caracteres.")
        if not isinstance(autor, str):
            raise ValueError("El autor debe ser una cadena de caracteres.")
        if not isinstance(genero, str):
            raise ValueError("El género debe ser una cadena de caracteres.")
        if not isinstance(ano_publicacion, int):
            raise ValueError("El año de publicación debe ser un número entero.")
        if not isinstance(isbn, int):
            raise ValueError("El ISBN debe ser un número entero.")

        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano_publicacion = ano_publicacion
        self.isbn = isbn
    
    # Métodos getter para acceder a los atributos públicos
    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_genero(self):
        return self.genero

    def get_ano_publicacion(self):
        return self.ano_publicacion

    def get_isbn(self):
        return self.isbn
    
    # Método para convertir el objeto Libro a un diccionario
    
    
    def toDiccionario(self):
        """
        Convierte el objeto Libro a un diccionario.

        Returns:
        dict: Un diccionario que representa el objeto Libro.
        """
        return {
            "Título": self.titulo,
            "Autor": self.autor,
            "Género": self.genero,
            "Año de Publicación": self.ano_publicacion,
            "ISBN": self.isbn,
        }
    
    @classmethod
    def fromDiccionario(cls, dicc):
        """
        Crea un objeto Libro a partir de un diccionario.

        Args:
        dicc (dict): Un diccionario que contiene los atributos del libro.

        Returns:
        Libro: Un objeto Libro creado a partir del diccionario.
        """
        if not isinstance(dicc, dict):
            raise ValueError("El diccionario debe ser un objeto de tipo dict.")
        return cls(
            dicc["titulo"],
            dicc["autor"],
            dicc["genero"],
            dicc["ano_publicacion"],
            dicc["isbn"],
        )
