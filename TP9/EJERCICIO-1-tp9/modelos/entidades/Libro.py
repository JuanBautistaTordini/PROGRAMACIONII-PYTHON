'''
+---------------------+
|     Clase Libro     |
+---------------------+
| - ISBN: int         |
| - titulo: str       |
| - autor: str        |
| - genero: str       |
| - anio_publicacion: int|
| - cantidad_ejemplares: int|
+---------------------+
| <<metodos de clase>>|
| + fromDiccionario(dic: Diccionario): Libro|
| <<metodos de instancia>>|
| +Libro(isbn: int, titulo: str, autor: str, genero: str, anio_publicacion: int)|
| <<consultas triviales>>|
| <<comandos triviales>>|
| +esIgual(otro: Libro): bool|
| +toString(): str|
| +toDiccionario(): diccionario|
+---------------------+
'''

class Libro:
    #Constructor
    def __init__(self, isbn:int, titulo:str, autor:str, genero:str, anio_publicacion:int):
        #validaciones
        
        if not isinstance(isbn, int):
            raise ValueError("El ISBN debe ser un numero entero")
        if not isinstance(titulo, str):
            raise ValueError("El titulo debe ser una cadena de caracteres")
        if not isinstance(autor, str):
            raise ValueError("El autor debe ser una cadena de caracteres")
        if not isinstance(genero, str):
            raise ValueError("El genero debe ser una cadena de caracteres")
        if not isinstance(anio_publicacion, int):
            raise ValueError("El año de publicacion debe ser un numero entero")
        
        #atributos de instancia
        
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio_publicacion = anio_publicacion
        self.cantidad_ejemplares = 0
    
    #Metodos de clase
    @classmethod
    def fromDiccionario(cls, dic:dict):
        return cls(
            dic['isbn'], 
            dic['titulo'], 
            dic['autor'], 
            dic['genero'], 
            dic['anio_publicacion']
        )
    
    #Consultas triviales
    def getISBN(self):
        return self.isbn
    
    def getTitulo(self):
        return self.titulo
    
    def getAutor(self):
        return self.autor
    
    def getGenero(self):
        return self.genero
    
    def getAnioPublicacion(self):
        return self.anio_publicacion
    
    def getCantidadEjemplares(self):
        return self.cantidad_ejemplares
    
    #comandos triviales
    def setISBN(self, isbn:int):
        self.isbn = isbn
    
    def setTitulo(self, titulo:str):
        self.titulo = titulo
    
    def setAutor(self, autor:str):
        self.autor = autor
    
    def setGenero(self, genero:str):
        self.genero = genero
    
    def setAnioPublicacion(self, anio_publicacion:int):
        self.anio_publicacion = anio_publicacion
    
    def setCantidadEjemplares(self, cantidad_ejemplares:int):
        self.cantidad_ejemplares = cantidad_ejemplares
    
    #Metodos de instancia
    def esIgual(self, otro):
        return self.isbn == otro.isbn

    #toString
    def __str__(self):
        return f"ISBN: {self.isbn}, Titulo: {self.titulo}, Autor: {self.autor}, Genero: {self.genero}, Año de publicacion: {self.anio_publicacion}, Cantidad de ejemplares: {self.cantidad_ejemplares}"

    def toDiccionario(self):
        return {
            'isbn': self.isbn,
            'titulo': self.titulo,
            'autor': self.autor,
            'genero': self.genero,
            'anio_publicacion': self.anio_publicacion
        }
    
    