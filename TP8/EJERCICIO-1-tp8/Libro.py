class Libro:
    def __init__(self, titulo: str, autor: str, genero: str, ano_publicacion: int, isbn: int):
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
        return {
            "Título": self.titulo,
            "Autor": self.autor,
            "Género": self.genero,
            "Año de Publicación": self.ano_publicacion,
            "ISBN": self.isbn,
        }
    
    @classmethod
    def fromDiccionario(cls, dicc):
        return cls(
            dicc["titulo"],
            dicc["autor"],
            dicc["genero"],
            dicc["ano_publicacion"],
            dicc["isbn"],
        )
