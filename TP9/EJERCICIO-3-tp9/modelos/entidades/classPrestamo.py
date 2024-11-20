'''
+-----------------------+
|     Prestamo          |
+-----------------------+
| <<atributos de clase>>|
| - ultimoId: int       |
+-----------------------+
| <<atributos de instancia>>|
| - id: int             |
| - socio_dni: int      |
| - libro_isbn: int     |
| - fecha_retiro: date  |
| - cant_dias: int      |
| - fecha_devolucion: date|
+-----------------------+
| <<metodos de clase>>  |
| + obtenerNuevoId(): int|
| + establecerUltimoId(id: int)|
| + fromDiccionario(dic: Diccionario) : Prestamo|
+-----------------------+
| <<metodos de instancia>>|
| + Prestamo(socio_dni: int, libro_isbn: int, fecha_retiro: date, cant_dias: int)|
| + Prestamo(id: int, socio_dni: int, libro_isbn: int, fecha_retiro: date, cant_dias: int)|
| + establecerSocioDNI(socio_dni: int)|
| + establecerLibroISBN(isbn: int)|
| + establecerFechaRetiro(fecha: date)|
| + establecerCantDias(cant: int)|
| + establecerFechaDevolucion(fecha: date)|
| + obtenerSocioDNI(): int|
| + obtenerISBN(): int|
| + obtenerFechaRetiro(): date|
| + obtenerCantDias(): int|
| + obtenerFechaDevolucion(): date|
| + esIgual(otro: Prestamo): bool|
| + __str__(): str|
| + toDiccionario(): diccionario|
+-----------------------+

OBSERVACIONES:

- Los prestamos se identifican por la clave (socio_dni, libro_isbn, fecha_retiro)

- obtenerNuevoId(): int se utiliza para obtener un ID unico para cada nueva instancia, incrementa el atributo de clase ultimoID y lo retorna.

- establecerUltimoId(id: int) se utiliza cuando inicia el sistema y establece el ultimo id utilizando o 0 si no se encuentra el archivo de datos.
'''

from datetime import datetime

class Prestamo:
    # atributos de clase
    ultimoId = 0
    
    # atributos de instancia
    def __init__(self, socio_dni: int, libro_isbn: int, fecha_retiro: datetime, cant_dias: int, fecha_devolucion: datetime):
        # validaciones:
        if not isinstance(socio_dni, int):
            raise ValueError("El dni del socio debe ser un entero.")
        if not isinstance(libro_isbn, int):
            raise ValueError("El ISBN del libro debe ser un entero.")
        if not isinstance(fecha_retiro, datetime):
            raise ValueError("La fecha de retiro debe ser un objeto datetime.")
        if not isinstance(cant_dias, int):
            raise ValueError("La cantidad de dias debe ser un entero.")
        if not isinstance(fecha_devolucion, datetime):
            raise ValueError("La fecha de devolucion debe ser un objeto datetime.")
        
        # asignaciones
        self.id = Prestamo.obtenerNuevoId()
        self.socio_dni = socio_dni
        self.libro_isbn = libro_isbn
        self.fecha_retiro = fecha_retiro
        self.cant_dias = cant_dias
        self.fecha_devolucion = None
        
    #metodos de clase
    @classmethod
    def obtenerNuevoId(cls) -> int:
        cls.ultimoId += 1
        return cls.ultimoId
    
    @classmethod
    def establecerUltimoId(cls, id: int):
        cls.ultimoId = id
        
    @classmethod
    def fromDiccionario(cls, dic: dict) -> 'Prestamo':
        prestamo = Prestamo(
            dic['socio_dni'],
            dic['libro_isbn'],
            dic['fecha_retiro'],
            dic['cant_dias'],
            dic['fecha_devolucion']
            dic['id']
        )
    
    #metodos de instancia
    def establecerSocioDNI(self, socio_dni: int):
        self.socio_dni = socio_dni
    
    def establecerLibroISBN(self, isbn: int):
        self.libro_isbn = isbn
    
    def establecerFechaRetiro(self, fecha: datetime):
        self.fecha_retiro = fecha
    
    def establecerCantDias(self, cant: int):
        self.cant_dias = cant
    
    def establecerFechaDevolucion(self, fecha: datetime):
        self.fecha_devolucion = fecha
    
    def obtenerSocioDNI(self) -> int:
        return self.socio_dni
    
    def obtenerISBN(self) -> int:
        return self.libro_isbn
    
    def obtenerFechaRetiro(self) -> datetime:
        return self.fecha_retiro
    
    def obtenerCantDias(self) -> int:
        return self.cant_dias
    
    def obtenerFechaDevolucion(self) -> datetime:
        return self.fecha_devolucion
    
    def esIgual(self, otro: 'Prestamo') -> bool:
        return self.id == otro.id
    
    def __str__(self) -> str:
        return f"Prestamo {self.id}: {self.socio_dni} - {self.libro_isbn} - {self.fecha_retiro} - {self.cant_dias} - {self.fecha_devolucion}"
    
    def toDiccionario(self) -> dict:
        return {
            'id': self.id,
            'socio_dni': self.socio_dni,
            'libro_isbn': self.libro_isbn,
            'fecha_retiro': self.fecha_retiro,
            'cant_dias': self.cant_dias,
            'fecha_devolucion': self.fecha_devolucion
        }
        